from operator import and_

from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.state_helper import set_state, State, clear_state
from bot.helpers.user_helper import reply_to
from database import session
from i18n import get_language_token, Token
from models import Submission, User, SubmissionCategory, ReviewCategory
from api.review import add_review


def user_not_in_reviewers(submission: Submission, user: User) -> bool:
    all_reviewer_names = [x.user.username for x in submission.reviews]
    return user.username not in all_reviewer_names


def main_review_handler(user: User, update: Update, context: CallbackContext):
    set_state(context, State.REVIEWING)

    if "submission" in context.user_data:
        _review_answer_handler(user, update, context)
        return

    _send_submission_to_review(user, update, context)


def _send_submission_to_review(user: User, update: Update, context: CallbackContext):
    submissions = session.query(Submission).filter(
        and_(Submission.user_id != user.id, Submission.language == user.language)).all()
    submissions = sorted(submissions, key=lambda x: x.review_count, reverse=True)
    submissions = [x for x in submissions if user_not_in_reviewers(x, user)]

    if len(submissions) > 0:
        submission: Submission = submissions[0]
        context.user_data["submission"] = submission

        if submission.category == SubmissionCategory.POSITIVE_SEPARATED or \
                submission.category == SubmissionCategory.POSITIVE_TOGETHER:
            review_question = get_language_token(user.language, Token.REVIEW_QUESTION_POSITIVE)\
                              % (submission.value, ",".join(submission.mwe_words))
            reply_to(user, update, review_question,
                     Keyboard.review_keyboard(user.language))
        else:
            review_question = get_language_token(user.language, Token.REVIEW_QUESTION_NEGATIVE) \
                              % (submission.value, ",".join(submission.mwe_words))
            reply_to(user, update, review_question,
                     Keyboard.review_keyboard(user.language))
    else:
        clear_state(context)
        if "submission" in context.user_data:
            del context.user_data["submission"]
        reply_to(user, update, get_language_token(user.language, Token.NO_SUBMISSIONS),
                 Keyboard.main(user.language))


def _review_answer_handler(user: User, update: Update, context: CallbackContext):
    available_inputs = [
        get_language_token(user.language, Token.AGREE_NICE_EXAMPLE),
        get_language_token(user.language, Token.DO_NOT_LIKE_EXAMPLE),
        get_language_token(user.language, Token.SKIP_THIS_ONE),
        get_language_token(user.language, Token.QUIT_REVIEWING)
    ]

    if update.message.text not in available_inputs:
        reply_to(user, update,
                 get_language_token(user.language, Token.PLEASE_ENTER_VALID_REVIEW),
                 Keyboard.review_keyboard(user.language))
        return

    submission = context.user_data["submission"]

    if update.message.text == get_language_token(user.language, Token.AGREE_NICE_EXAMPLE):
        add_review(user, submission, ReviewCategory.LIKE)
    elif update.message.text == get_language_token(user.language, Token.DO_NOT_LIKE_EXAMPLE):
        add_review(user, submission, ReviewCategory.DISLIKE)
    elif update.message.text == get_language_token(user.language, Token.SKIP_THIS_ONE):
        add_review(user, submission, ReviewCategory.SKIP)
    else:
        reply_to(user, update,
                 get_language_token(user.language, Token.OPERATION_CANCELLED),
                 Keyboard.main(user.language))
        del context.user_data["submission"]
        clear_state(context)
        return

    _send_submission_to_review(user, update, context)
