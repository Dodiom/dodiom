import time
from datetime import datetime
from operator import and_
from typing import List

from telegram import Update
from telegram.ext import CallbackContext

from api.achievements import award_achievement
from api.mwe import get_todays_mwe
from api.user import unmute_user, mute_user, update_user
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.notification_manager import notification_manager
from bot.helpers.scoreboard import scoreboard
from bot.helpers.state_helper import set_state, State, clear_state
from bot.helpers.submission_scores import submission_scores
from bot.helpers.user_helper import reply_to, reply_html
from bot.stickers import ACHIEVEMENT_STICKER
from config import mwexpress_config
from database import database
from i18n import Token, get_random_congrats_message
from models import Submission, User, SubmissionCategory, ReviewCategory, Mwe, Review, AchievementType
from api.review import add_review
from nlp.parsing import parser


def get_submissions_to_review(mwe: Mwe, user: User) -> List[Submission]:
    session = database.get_session()
    submissions = session.query(Submission) \
        .filter(Submission.user != user) \
        .filter(Submission.mwe == mwe) \
        .filter(Submission.flagged == False) \
        .all()
    reviews_made_by_user = session.query(Review) \
        .filter(Review.user == user) \
        .filter(Review.mwe == mwe) \
        .all()
    reviews_made_by_user_sub_ids = [x.submission_id for x in reviews_made_by_user]
    submissions = sorted(submissions, key=lambda x: x.review_count)
    return [x for x in submissions if x.id not in reviews_made_by_user_sub_ids]


def main_review_handler(user: User, update: Update, context: CallbackContext):
    now = datetime.now().time()
    if mwexpress_config.start_time <= now < mwexpress_config.end_time:
        set_state(context, State.REVIEWING)

        if "submission" in context.user_data:
            _review_answer_handler(user, update, context)
            return

        _send_submission_to_review(user, update, context)
    else:
        clear_state(context)
        unmute_user(user.id)
        _safe_delete_context_data(context, "submission")
        _safe_delete_context_data(context, "review_count")
        reply_to(user, update, user.language.get(Token.GAME_HOURS_FINISHED) % mwexpress_config.start_time.hour,
                 reply_markup=Keyboard.main(user))


def _send_submission_to_review(user: User, update: Update, context: CallbackContext):
    if not user.viewed_review_help:
        reply_to(user, update, user.language.get(Token.REVIEW_HELP_MESSAGE_1))
        time.sleep(4)
        reply_to(user, update, user.language.get(Token.REVIEW_HELP_MESSAGE_2))
        time.sleep(4)
        user.viewed_review_help = True
        update_user(user)

    todays_mwe = get_todays_mwe(user.language)
    submissions = get_submissions_to_review(todays_mwe, user)

    if len(submissions) > 0:
        submission: Submission = submissions[0]
        context.user_data["submission"] = submission
        if "review_count" not in context.user_data:
            context.user_data["review_count"] = 0

        parsed = parser.parse(submission.value, submission.mwe)
        review_example = submission.value
        for index in reversed(sorted(submission.mwe_indices)):
            start_index = parsed.token_positions[index][0]
            end_index = parsed.token_positions[index][1]
            review_example = review_example[:end_index] + "</u></b>" + review_example[end_index:]
            review_example = review_example[:start_index] + "<b><u>" + review_example[start_index:]

        if submission.category == SubmissionCategory.POSITIVE_SEPARATED or \
                submission.category == SubmissionCategory.POSITIVE_TOGETHER:
            review_question = user.language.get(Token.REVIEW_QUESTION_POSITIVE) \
                              % (review_example, _get_word_list_str_from_submission(submission))
            reply_html(user, update, review_question,
                       Keyboard.review_keyboard(user.language))
        else:
            review_question = user.language.get(Token.REVIEW_QUESTION_NEGATIVE) \
                              % (review_example, _get_word_list_str_from_submission(submission))
            reply_html(user, update, review_question,
                       Keyboard.review_keyboard(user.language))
    else:
        if "review_count" in context.user_data:
            reply_to(user, update, user.language.get(Token.NO_SUB_LEFT_TO_REVIEW),
                     Keyboard.main(user))
        else:
            reply_to(user, update, user.language.get(Token.NO_SUBMISSIONS),
                     Keyboard.main(user))
        clear_state(context)
        unmute_user(user.id)
        _safe_delete_context_data(context, "submission")
        _safe_delete_context_data(context, "review_count")


def _get_word_list_str_from_submission(submission: Submission):
    mwe_words = [f"<b><u>{x}</u></b>" for x in submission.mwe_words]
    first_ones = mwe_words[:-1]
    last_one = mwe_words[-1]
    return f'{", ".join(first_ones)} {submission.language.get(Token.AND)} {last_one}'


def _review_answer_handler(user: User, update: Update, context: CallbackContext):
    mute_user(user.id)
    available_inputs = [
        user.language.get(Token.AGREE_NICE_EXAMPLE),
        user.language.get(Token.DO_NOT_LIKE_EXAMPLE),
        user.language.get(Token.REPORT_SUBMISSION),
        user.language.get(Token.QUIT_REVIEWING)
    ]

    if update.message.text not in available_inputs:
        reply_to(user, update,
                 user.language.get(Token.PLEASE_ENTER_VALID_REVIEW),
                 Keyboard.review_keyboard(user.language))
        return

    submission = context.user_data["submission"]
    context.user_data["review_count"] += 1

    if update.message.text == user.language.get(Token.AGREE_NICE_EXAMPLE):
        add_review(user, submission, ReviewCategory.LIKE)
        reply_to(user, update,
                 user.language.get(Token.THANKS_FOR_REVIEW) % (get_random_congrats_message(user.language), submission_scores.get_review_score()))
        _process_review_achievements(user, update)
        notification_manager.send_someone_liked_your_example(submission.user, context)
        scoreboard.iterate(update, context)
    elif update.message.text == user.language.get(Token.DO_NOT_LIKE_EXAMPLE):
        add_review(user, submission, ReviewCategory.DISLIKE)
        reply_to(user, update,
                 user.language.get(Token.THANKS_FOR_REVIEW) % (get_random_congrats_message(user.language), submission_scores.get_review_score()))
        _process_review_achievements(user, update)
        scoreboard.iterate(update, context)
    elif update.message.text == user.language.get(Token.REPORT_SUBMISSION):
        add_review(user, submission, ReviewCategory.SKIP)
        reply_to(user, update,
                 user.language.get(Token.REPORT_SUBMISSION_REPLY))
        context.bot.send_message(mwexpress_config.moderator,
                                 f"Someone reported this submission: {submission.value}\n"
                                 f"Flag submission: /flag{submission.id}, "
                                 f"ban user: /ban{submission.user.id}")
        _process_review_achievements(user, update)
        scoreboard.iterate(update, context)
    else:
        unmute_user(user.id)
        reply_to(user, update,
                 user.language.get(Token.REVIEW_CANCELLED),
                 Keyboard.main(user))
        _safe_delete_context_data(context, "submission")
        clear_state(context)
        return

    _send_submission_to_review(user, update, context)


def _process_review_achievements(user: User, update: Update):
    session = database.get_session()
    todays_mwe = get_todays_mwe(user.language)
    user_review_count_today = session.query(Review)\
        .filter(and_(Review.mwe == todays_mwe, Review.user == user)).count()
    if user_review_count_today == 10:
        award_achievement(user, AchievementType.REVIEW_LVL_1)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.REVIEW_LVL_1_ACH_CONGRATS_MSG))
    if user_review_count_today == 20:
        award_achievement(user, AchievementType.REVIEW_LVL_2)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.REVIEW_LVL_2_ACH_CONGRATS_MSG))
    if user_review_count_today == 40:
        award_achievement(user, AchievementType.REVIEW_LVL_3)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.REVIEW_LVL_3_ACH_CONGRATS_MSG))
    if user_review_count_today == 80:
        award_achievement(user, AchievementType.REVIEW_LVL_4)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.REVIEW_LVL_4_ACH_CONGRATS_MSG))
    if user_review_count_today == 160:
        award_achievement(user, AchievementType.REVIEW_LVL_5)
        update.message.reply_sticker(ACHIEVEMENT_STICKER)
        update.message.reply_html(user.language.get(Token.REVIEW_LVL_5_ACH_CONGRATS_MSG))


def _safe_delete_context_data(context: CallbackContext, name: str) -> None:
    if name in context.user_data:
        del context.user_data[name]
