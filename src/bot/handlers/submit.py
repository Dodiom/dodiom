from typing import List, Dict

from stanza.models.common.doc import Sentence
from telegram import Update
from telegram.ext import CallbackContext

from api.mwe import get_todays_mwe
from api.submission import add_submission_using_doc
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.state_helper import set_state, State, clear_state
from bot.helpers.user_helper import reply_to
from i18n import get_language_token, Token, get_random_congrats_message
from models import User, Mwe
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
    -> Ask user if parts of the MWE occur more than once.
3. Get category from user
    -> 
"""


def main_submit_handler(user: User, update: Update, context: CallbackContext):
    set_state(context, State.SUBMISSION)
    sub_state = context.user_data["sub_state"] \
        if "sub_state" in context.user_data \
        else None

    if sub_state is None:
        start_submit_handler(user, update, context)
    elif sub_state == "typing_example":
        submit_message_handler(user, update, context)
    elif sub_state == "handle_multiple_occurrence":
        mwe_position_multiple_occurrence_handler(user, update, context, False)
    elif sub_state == "choosing_category":
        submit_category_handler(user, update, context)


def start_submit_handler(user: User, update: Update, context: CallbackContext) -> None:
    """ Starts the submission cycle for user. """
    todays_mwe = get_todays_mwe(user.language)
    context.user_data["sub_state"] = "typing_example"
    reply_to(user, update,
             get_language_token(user.language, Token.PLEASE_ENTER_EXAMPLE) % todays_mwe.name,
             reply_markup=Keyboard.remove())


def submit_message_handler(user: User, update: Update, context: CallbackContext) -> None:
    """ Gets the submission text from user """
    todays_mwe = get_todays_mwe(user.language)

    submission_value = update.message.text
    context.user_data["submission_value"] = submission_value
    doc = process_sentence(user.language, submission_value)
    context.user_data["doc"] = doc

    if len(doc.sentences) > 1:
        reply_to(user, update,
                 get_language_token(user.language, Token.PLEASE_ENTER_ONE_SENTENCE) % len(doc.sentences))
        return

    submission_lemmas = [x.lemma for x in doc.iter_words()]
    context.user_data["submission_lemmas"] = submission_lemmas
    submission_words = [x.text for x in doc.iter_words()]
    context.user_data["submission_words"] = submission_words

    if not submission_contains_mwe(todays_mwe, submission_lemmas):
        reply_to(user, update,
                 get_language_token(user.language, Token.SUBMISSION_DOES_NOT_CONTAIN_MWE) % todays_mwe.name)
        return

    # Find MWE position
    mwe_lemma_positions = dict()
    for mwe_lemma in todays_mwe.lemmas:
        mwe_lemma_positions[mwe_lemma] = []
        for ix, lemma in enumerate(submission_lemmas):
            if lemma == mwe_lemma:
                mwe_lemma_positions[mwe_lemma].append(ix)

    context.user_data["mwe_lemma_positions"] = mwe_lemma_positions

    if any([len(x) > 1 for x in mwe_lemma_positions.values()]):
        context.user_data["sub_state"] = "handle_multiple_occurrence"
        mwe_position_multiple_occurrence_handler(user, update, context, True)
        return

    # TODO: Check if mwe is submitted before, don't allow duplicates

    submission_mwe_lemmas = [submission_words[x] for x in [x[0] for x in mwe_lemma_positions.values()]]
    submission_mwe_lemmas_str = ", ".join(submission_mwe_lemmas[:-1])
    submission_mwe_lemmas_str += "* %s *%s" % (get_language_token(user.language, Token.AND), submission_mwe_lemmas[-1])

    context.user_data["sub_state"] = "choosing_category"
    reply_to(user, update,
             get_language_token(user.language, Token.DOES_WORDS_FORM_SPECIAL_MEANING) % submission_mwe_lemmas_str,
             Keyboard.submission_category(user.language))


def mwe_position_multiple_occurrence_handler(user: User, update: Update,
                                             context: CallbackContext,
                                             called_from_another_handler: bool) -> None:
    mwe_lemma_positions: Dict[str, List] = context.user_data["mwe_lemma_positions"]
    doc = context.user_data["doc"]
    sentence: Sentence = doc.sentences[0]
    todays_mwe = get_todays_mwe(user.language)

    if not called_from_another_handler:
        current_multiple_occurrence = context.user_data["current_multiple_occurrence"]
        message = update.message.text
        if not message.isdigit():
            reply_to(user, update,
                     get_language_token(user.language, Token.ENTER_VALID_COMMAND))
            return
        if not (1 <= int(message) <= len(mwe_lemma_positions[current_multiple_occurrence])):
            reply_to(user, update,
                     get_language_token(user.language, Token.ENTER_VALID_COMMAND))
            return
        mwe_lemma_positions[current_multiple_occurrence] = [
            mwe_lemma_positions[current_multiple_occurrence][int(message) - 1]]

    for lemma, lemma_positions in mwe_lemma_positions.items():
        if len(lemma_positions) > 1:
            context.user_data["current_multiple_occurrence"] = lemma
            reply_to(user, update,
                     get_language_token(user.language, Token.MULTIPLE_LEMMA_OCCURRENCE) % lemma,
                     reply_markup=Keyboard.numeric_keyboard(1, len(lemma_positions)))
            ret_sentence = context.user_data["submission_value"]
            ix = len(lemma_positions)
            for lemma_pos in reversed(lemma_positions):
                ret_sentence = ret_sentence[:sentence.tokens[lemma_pos].end_char] + "(" + str(ix) + ")" + ret_sentence[
                                                                                                          sentence.tokens[
                                                                                                              lemma_pos].end_char:]
                ix -= 1
            reply_to(user, update, ret_sentence, Keyboard.numeric_keyboard(1, len(lemma_positions)))
            return

    submission_words = [x.text for x in doc.iter_words()]
    submission_mwe_lemmas = [submission_words[x] for x in [x[0] for x in mwe_lemma_positions.values()]]
    submission_mwe_lemmas_str = ", ".join(submission_mwe_lemmas[:-1])
    submission_mwe_lemmas_str += "* %s *%s" % (get_language_token(user.language, Token.AND), submission_mwe_lemmas[-1])

    context.user_data["sub_state"] = "choosing_category"
    reply_to(user, update,
             get_language_token(user.language, Token.DOES_WORDS_FORM_SPECIAL_MEANING) % submission_mwe_lemmas_str,
             Keyboard.submission_category(user.language))


def submit_category_handler(user: User, update: Update, context: CallbackContext) -> None:
    available_inputs = [
        get_language_token(user.language, Token.FORMS_SPECIAL_MEANING),
        get_language_token(user.language, Token.DOES_NOT_FORM_SPECIAL_MEANING),
        get_language_token(user.language, Token.CANCEL)
    ]
    if update.message.text not in available_inputs:
        reply_to(user, update,
                 get_language_token(user.language, Token.ENTER_VALID_MWE_CATEGORY),
                 Keyboard.submission_category(user.language))
        return

    if update.message.text == get_language_token(user.language, Token.CANCEL):
        clear_state(context)
        reply_to(user, update,
                 get_language_token(user.language, Token.OPERATION_CANCELLED),
                 Keyboard.main(user.language))
        return

    mwe_lemma_positions = context.user_data["mwe_lemma_positions"]
    mwe_indices = [x[0] for x in mwe_lemma_positions.values()]

    doc = context.user_data["doc"]
    todays_mwe = get_todays_mwe(user.language)
    positive = update.message.text == get_language_token(user.language, Token.FORMS_SPECIAL_MEANING)
    submission = add_submission_using_doc(user, doc, todays_mwe, mwe_indices, positive)

    clear_state(context)
    del context.user_data["sub_state"]
    del context.user_data["submission_value"]
    del context.user_data["submission_lemmas"]
    del context.user_data["submission_words"]
    del context.user_data["doc"]
    del context.user_data["mwe_lemma_positions"]

    reply_to(user, update,
             get_language_token(user.language, Token.THANKS_FOR_SUBMISSION) % (
                 get_random_congrats_message(user.language), submission.points),
             Keyboard.main(user.language))


def submission_contains_mwe(mwe: Mwe, submission: List[str]) -> bool:
    for mwe_lemma in mwe.lemmas:
        if mwe_lemma not in submission:
            return False
    return True
