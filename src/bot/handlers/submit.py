import random
import time
from datetime import datetime
from typing import List
import itertools

from telegram import Update
from telegram.ext import CallbackContext

from api.mwe import get_todays_mwe
from api.submission import add_submission_using_doc
from api.user import mute_user, unmute_user, update_user
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.state_helper import set_state, State, clear_state
from bot.helpers.tip_helper import send_hint_message
from bot.helpers.user_helper import reply_to, reply_html
from config import mwexpress_config
from i18n import Token, get_random_congrats_message, Language
from models import User, Mwe
from nlp.language_helper import lowercase
from nlp.stanza import process_sentence

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
    todays_mwe = get_todays_mwe(user.language)

    submission_value = update.message.text
    context.user_data["submission_value"] = submission_value
    doc = process_sentence(user.language, submission_value)
    context.user_data["doc"] = doc

    if len(doc.sentences) > 1:
        reply_to(user, update,
                 user.language.get(Token.PLEASE_ENTER_ONE_SENTENCE) % len(doc.sentences))
        return

    submission_lemmas = [lowercase(x.lemma, user.language) for x in doc.iter_words()]
    context.user_data["submission_lemmas"] = submission_lemmas
    submission_words = [x.text for x in doc.iter_words()]
    context.user_data["submission_words"] = submission_words

    if not submission_contains_mwe(todays_mwe, submission_lemmas):
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
    mwe_lemma_positions = dict()
    for ix_tm, mwe_lemma in enumerate(todays_mwe.lemmas):
        mwe_lemma_positions[mwe_lemma] = []
        for ix, lemma in enumerate(submission_lemmas):
            if lemma == mwe_lemma or check_turkish_mastar(todays_mwe, ix_tm, lemma):
                mwe_lemma_positions[mwe_lemma].append(ix)

    mwe_instances = list(itertools.product(*[x for x in mwe_lemma_positions.values()]))
    mwe_instances = sorted(mwe_instances, key=lambda x: max(x) - min(x))

    mwe_indices = mwe_instances[0]
    context.user_data["mwe_indices"] = mwe_indices

    submission_mwe_lemmas = [submission_words[x] for x in [x[0] for x in mwe_lemma_positions.values()]]
    submission_mwe_lemmas_str = ", ".join(submission_mwe_lemmas[:-1])
    submission_mwe_lemmas_str += "</u></b> %s <b><u>%s" % (user.language.get(Token.AND), submission_mwe_lemmas[-1])

    context.user_data["sub_state"] = "choosing_category"
    reply_html(user, update,
               user.language.get(Token.DOES_WORDS_FORM_SPECIAL_MEANING) % submission_mwe_lemmas_str,
               Keyboard.submission_category(user.language))


def submission_contains_todays_mwe(user: User, submission: str) -> bool:
    todays_mwe = get_todays_mwe(user.language)
    submission_value = submission
    doc = process_sentence(user.language, submission_value)
    if len(doc.sentences) > 1:
        return False
    submission_lemmas = [lowercase(x.lemma, user.language) for x in doc.iter_words()]
    if not submission_contains_mwe(todays_mwe, submission_lemmas):
        return False
    return True


def check_turkish_mastar(mwe: Mwe, ix_tm: int, submission_lemma: str):
    return mwe.language == Language.TURKISH and \
           mwe.verb_indices[ix_tm] and (submission_lemma == mwe.lemmas[ix_tm] + "mek" or
                                        submission_lemma == mwe.lemmas[ix_tm] + "mak")


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
        clear_state(context)
        unmute_user(user.id)
        reply_to(user, update,
                 user.language.get(Token.SUBMISSION_CANCELLED),
                 Keyboard.main(user.language))
        return

    mwe_indices = context.user_data["mwe_indices"]

    doc = context.user_data["doc"]
    todays_mwe = get_todays_mwe(user.language)
    positive = update.message.text == user.language.get(Token.FORMS_SPECIAL_MEANING)
    submission = add_submission_using_doc(user, doc, todays_mwe, mwe_indices, positive)

    unmute_user(user.id)
    _clear_context(context)

    reply_to(user, update,
             user.language.get(Token.THANKS_FOR_SUBMISSION) % (
                 get_random_congrats_message(user.language), submission.points),
             Keyboard.main(user.language))
    if random.random() < 0.5:
        time.sleep(1)
        send_hint_message(user, update, context)


def _clear_context(context: CallbackContext):
    clear_state(context)
    _safe_delete_context_data(context, "sub_state")
    _safe_delete_context_data(context, "submission_value")
    _safe_delete_context_data(context, "submission_lemmas")
    _safe_delete_context_data(context, "submission_words")
    _safe_delete_context_data(context, "doc")
    _safe_delete_context_data(context, "mwe_indices")


def submission_contains_mwe(mwe: Mwe, submission: List[str]) -> bool:
    for is_verb, mwe_lemma in zip(mwe.verb_indices, mwe.lemmas):
        if mwe.language == Language.ENGLISH:
            if mwe_lemma not in submission:
                return False
        elif mwe.language == Language.TURKISH:
            if not is_verb:
                if mwe_lemma not in submission:
                    return False
            else:
                if mwe_lemma not in submission \
                        and mwe_lemma + "mek" not in submission \
                        and mwe_lemma + "mak" not in submission:
                    return False
    return True


def _safe_delete_context_data(context: CallbackContext, name: str) -> None:
    if name in context.user_data:
        del context.user_data[name]
