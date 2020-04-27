from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.mwe_helper import get_todays_mwe
from bot.helpers.state_helper import set_state, State, clear_state
from bot.helpers.user_helper import reply_to
from database import session
from i18n import get_language_token, Token, get_random_congrats_message, Language
from models import User, Submission, Mwe, SubmissionCategory
from nlp.lemma import get_lemmas, get_words


def submit_handler(user: User, update: Update, context: CallbackContext) -> None:
    """ Starts the submission cycle for user. """
    todays_mwe = get_todays_mwe(user.language)
    reply_to(user, update,
             get_language_token(user.language, Token.PLEASE_ENTER_EXAMPLE) % todays_mwe.name,
             reply_markup=Keyboard.remove())
    set_state(context, State.TYPING_EXAMPLE)


def submit_message_handler(user: User, update: Update, context: CallbackContext) -> None:
    """ Gets the submission text from user """
    todays_mwe = get_todays_mwe(user.language)

    submission = Submission(
        value=update.message.text,
        lemmas=get_lemmas(user.language, update.message.text),
        words=get_words(user.language, update.message.text),
        language=user.language,
        user=user,
        mwe=todays_mwe,
        points=0
    )

    if not submission_contains_mwe(todays_mwe, submission):
        reply_to(user, update,
                 get_language_token(user.language, Token.SUBMISSION_DOES_NOT_CONTAIN_MWE) % todays_mwe.name)
        return

    # TODO: Check if mwe is submitted before, don't allow duplicates

    context.user_data["submission"] = submission
    set_state(context, State.CHOOSING_SUBMISSION_CATEGORY)

    submission_mwe_lemmas = [submission.words[x] for x in range(len(submission.lemmas)) if submission.lemmas[x] in todays_mwe.lemmas]
    submission_mwe_lemmas_str = ", ".join(submission_mwe_lemmas[:-1])
    submission_mwe_lemmas_str += "* %s *%s" % (get_language_token(user.language, Token.AND), submission_mwe_lemmas[-1])

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
        del context.user_data["submission"]
        reply_to(user, update,
                 get_language_token(user.language, Token.OPERATION_CANCELLED),
                 Keyboard.main(user.language))
        return

    submission = context.user_data["submission"]
    submission.category = get_submission_category(
        get_todays_mwe(user.language),
        submission,
        update.message.text == get_language_token(user.language, Token.FORMS_SPECIAL_MEANING)
    )
    submission.points = get_category_score(
        submission.language,
        submission.category
    )

    session.add(submission)
    session.commit()

    clear_state(context)

    reply_to(user, update,
             get_language_token(user.language, Token.THANKS_FOR_SUBMISSION) % (
                 get_random_congrats_message(user.language), submission.points),
             Keyboard.main(user.language))


def submission_contains_mwe(mwe: Mwe, submission: Submission) -> bool:
    for mwe_lemma in mwe.lemmas:
        if mwe_lemma not in submission.lemmas:
            return False
    return True


def get_submission_category(mwe: Mwe, submission: Submission, positive: bool) -> SubmissionCategory:
    submission_lemmas_bitmap = [(x in mwe.lemmas) for x in submission.lemmas]

    first_occurrence = submission_lemmas_bitmap.index(True)
    last_occurrence = len(submission_lemmas_bitmap) - 1 - submission_lemmas_bitmap[::-1].index(True)
    together = last_occurrence - first_occurrence == len(mwe.lemmas) - 1

    if together and positive:
        return SubmissionCategory.POSITIVE_TOGETHER
    elif not together and positive:
        return SubmissionCategory.POSITIVE_SEPARATED
    elif together and not positive:
        return SubmissionCategory.NEGATIVE_TOGETHER
    else:
        return SubmissionCategory.NEGATIVE_SEPARATED


def get_category_score(language: Language, category: SubmissionCategory) -> float:
    all_submissions = session\
        .query(Submission)\
        .filter(Submission.language == language)\
        .filter(Submission.category == category)\
        .filter(Submission.points > 0)\
        .all()
    category_initial_points = {
        SubmissionCategory.POSITIVE_TOGETHER: 10,
        SubmissionCategory.POSITIVE_SEPARATED: 20,
        SubmissionCategory.NEGATIVE_TOGETHER: 40,
        SubmissionCategory.NEGATIVE_SEPARATED: 30
    }
    return compound_interest(
        category_initial_points[category],
        -0.05,
        len(all_submissions)
    )


def compound_interest(p: int, r: float, n: float) -> float:
    return p * ((1 + r) ** n)
