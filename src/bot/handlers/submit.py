import random
import time
from datetime import datetime
from operator import and_

from telegram import Update
from telegram.ext import CallbackContext

from api.achievements import award_achievement, get_user_achievements
from api.mwe import get_todays_mwe
from api.submission import add_submission
from api.user import mute_user, unmute_user, update_user
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.state_helper import set_state, State, clear_state
from bot.helpers.submission_scores import submission_scores
from bot.helpers.tip_helper import send_hint_message
from bot.helpers.user_helper import reply_to, reply_html
from bot.stickers import ACHIEVEMENT_STICKER
from config import mwexpress_config
from database import database
from i18n import Token, get_random_congrats_message
from log import mwelog
from models import User, Mwe, Submission, AchievementType
from nlp.parsing import parser

"""
SUBMISSION
Main workflow:
1. Get user input
    -> Retry if MWE does not exist in the input
    -> Retry if submission contains more than one sentence
    -> Retry if submission is duplicate
    -> Retry if the submission language is different from the user language
2. Find MWE parts in submission and mark them
3. Get category from user
    -> 
"""


def main_submit_handler(user: User, update: Update, context: CallbackContext):
    set_state(context, State.SUBMISSION)
    sub_state = context.user_data["sub_state"] \
        if "sub_state" in context.user_data \
        else None

    now = datetime.now().time()
    if mwexpress_config.start_time <= now < mwexpress_config.end_time:
        mute_user(user.id)
        if sub_state is None:
            start_submit_handler(user, update, context)
        elif sub_state == "typing_example":
            submit_message_handler(user, update, context)
        elif sub_state == "choosing_category":
            submit_category_handler(user, update, context)
    else:
        unmute_user(user.id)
        _clear_context(context)
        reply_to(user, update, user.language.get(Token.GAME_HOURS_FINISHED) % mwexpress_config.start_time.hour,
                 reply_markup=Keyboard.main(user.language))


def start_submit_handler(user: User, update: Update, context: CallbackContext) -> None:
    """ Starts the submission cycle for user. """
    todays_mwe = get_todays_mwe(user.language)
    context.user_data["sub_state"] = "typing_example"
    if not user.viewed_submission_help:
        reply_html(user, update,
                   user.language.get(Token.SUBMISSION_HELP_MESSAGE_1))
        time.sleep(7)
        user.viewed_submission_help = True
        update_user(user)
    reply_html(user, update,
               user.language.get(Token.PLEASE_ENTER_EXAMPLE) % _get_word_list_str_from_mwe(todays_mwe),
               reply_markup=Keyboard.remove())


def _get_word_list_str_from_mwe(mwe: Mwe):
    mwe_words = [f"<b><u>{x}</u></b>" for x in mwe.lemmas]
    first_ones = mwe_words[:-1]
    last_one = mwe_words[-1]
    return f'{", ".join(first_ones)} {mwe.language.get(Token.AND)} {last_one}'


def submit_message_handler(user: User, update: Update, context: CallbackContext) -> None:
    """ Gets the submission text from user """
    submission_value = update.message.text

    sentence_count = parser.get_sentence_count(user.language, submission_value)
    if sentence_count != 1:
        reply_to(user, update,
                 user.language.get(Token.PLEASE_ENTER_ONE_SENTENCE) % sentence_count)
        return

    todays_mwe = get_todays_mwe(user.language)
    try:
        parsed = parser.parse(user.language, submission_value, "|".join(todays_mwe.lemmas))
    except Exception as ex:
        mwelog.error(ex)
        reply_to(user, update,
                 user.language.get(Token.SUBMISSION_CONTAINS_ERROR),
                 reply_markup=Keyboard.remove())
        return
    context.user_data["parsed"] = parsed

    if not parsed.contains_mwe(todays_mwe):
        reply_to(user, update,
                 user.language.get(Token.SUBMISSION_DOES_NOT_CONTAIN_MWE) % todays_mwe.name,
                 reply_markup=Keyboard.remove())
        return

    # Duplicate check
    # submission_hash = get_submission_hash(doc)
    # if session.query(Submission).filter(Submission.hash == submission_hash).count() > 0:
    #     reply_to(user, update,
    #              get_language_token(user.language, Token.DUPLICATE_SUBMISSION))
    #     return

    # Find MWE position

    submission_mwe_lemmas = parsed.get_mwe_tokens(todays_mwe)
    submission_mwe_lemmas_str = ", ".join(submission_mwe_lemmas[:-1])
    submission_mwe_lemmas_str += "</u></b> %s <b><u>%s" % (user.language.get(Token.AND), submission_mwe_lemmas[-1])

    context.user_data["sub_state"] = "choosing_category"
    reply_html(user, update,
               user.language.get(Token.DOES_WORDS_FORM_SPECIAL_MEANING) % submission_mwe_lemmas_str,
               Keyboard.submission_category(user.language))


def submission_contains_todays_mwe(user: User, submission: str) -> bool:
    todays_mwe = get_todays_mwe(user.language)
    if parser.get_sentence_count(user.language, submission) != 1:
        return False
    try:
        parsed = parser.parse(user.language, submission, "|".join(todays_mwe.lemmas))
        return parsed.contains_mwe(todays_mwe)
    except Exception as ex:
        mwelog.exception(str(ex))
        return False


def submit_category_handler(user: User, update: Update, context: CallbackContext) -> None:
    available_inputs = [
        user.language.get(Token.FORMS_SPECIAL_MEANING),
        user.language.get(Token.DOES_NOT_FORM_SPECIAL_MEANING),
        user.language.get(Token.CANCEL)
    ]
    if update.message.text not in available_inputs:
        reply_to(user, update,
                 user.language.get(Token.ENTER_VALID_MWE_CATEGORY),
                 Keyboard.submission_category(user.language))
        return

    if update.message.text == user.language.get(Token.CANCEL):
        _clear_context(context)
        unmute_user(user.id)
        reply_to(user, update,
                 user.language.get(Token.SUBMISSION_CANCELLED),
                 Keyboard.main(user.language))
        return

    parsed = context.user_data["parsed"]
    todays_mwe = get_todays_mwe(user.language)
    positive = update.message.text == user.language.get(Token.FORMS_SPECIAL_MEANING)
    submission = add_submission(user, parsed, todays_mwe, positive)

    unmute_user(user.id)
    _clear_context(context)

    reply_to(user, update,
             user.language.get(Token.THANKS_FOR_SUBMISSION) % (
                 get_random_congrats_message(user.language), submission.points),
             Keyboard.main(user.language))

    if random.random() < 0.5:
        time.sleep(1)
        send_hint_message(user, update, context)

    session = database.get_session()
    user_achievements = get_user_achievements(user)
    if session.query(Submission).filter(Submission.mwe == todays_mwe).count() == 1:
        # award first submission
        if AchievementType.FIRST_SUBMISSION not in user_achievements:
            award_achievement(user, AchievementType.FIRST_SUBMISSION)
            update.message.reply_sticker(ACHIEVEMENT_STICKER)
            update.message.reply_html(user.language.get(Token.FIRST_SUB_ACH_CONGRATS_MSG))

    now = datetime.now()
    start_datetime = datetime.combine(now, mwexpress_config.start_time)
    start_diff = now - start_datetime
    if start_diff.total_seconds() < 1800:
        # award early bird
        if AchievementType.EARLY_BIRD not in user_achievements:
            award_achievement(user, AchievementType.EARLY_BIRD)
            update.message.reply_sticker(ACHIEVEMENT_STICKER)
            update.message.reply_html(user.language.get(Token.EARLY_BIRD_ACH_CONGRATS_MSG))

    today_sub_count_by_user = session.query(Submission)\
        .filter(and_(Submission.mwe == todays_mwe, Submission.user == user)).count()
    if AchievementType.SUB_LVL_1 not in user_achievements and today_sub_count_by_user == 5:
        award_achievement(user, AchievementType.SUB_LVL_1)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.SUB_LVL_1_ACH_CONGRATS_MSG))
    if AchievementType.SUB_LVL_2 not in user_achievements and today_sub_count_by_user == 10:
        award_achievement(user, AchievementType.SUB_LVL_2)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.SUB_LVL_2_ACH_CONGRATS_MSG))
    if AchievementType.SUB_LVL_3 not in user_achievements and today_sub_count_by_user == 20:
        award_achievement(user, AchievementType.SUB_LVL_3)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.SUB_LVL_3_ACH_CONGRATS_MSG))
    if AchievementType.SUB_LVL_4 not in user_achievements and today_sub_count_by_user == 40:
        award_achievement(user, AchievementType.SUB_LVL_4)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.SUB_LVL_4_ACH_CONGRATS_MSG))
    if AchievementType.SUB_LVL_5 not in user_achievements and today_sub_count_by_user == 70:
        award_achievement(user, AchievementType.SUB_LVL_5)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.SUB_LVL_5_ACH_CONGRATS_MSG))

    submission_scores.iterate(context)


def _clear_context(context: CallbackContext):
    clear_state(context)
    _safe_delete_context_data(context, "sub_state")
    _safe_delete_context_data(context, "parsed")


def _safe_delete_context_data(context: CallbackContext, name: str) -> None:
    if name in context.user_data:
        del context.user_data[name]
