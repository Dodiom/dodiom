from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.mwe_helper import get_todays_mwe
from bot.helpers.user_helper import reply_to
from i18n import Token, get_language_token
from database import database
from models import Submission, SubmissionCategory, User
from operator import and_


def user_not_in_reviewers(submission: Submission, user: User) -> bool:
    all_reviewer_names = [x.user.username for x in submission.reviews]
    return user.username not in all_reviewer_names


def review_handler(user: User, update: Update, context: CallbackContext):
    session = database.get_session()
    submissions = session.query(Submission).filter(and_(Submission.user_id != user.id, Submission.language == user.language)).all()
    submissions = sorted(submissions, key=lambda x: x.review_count, reverse=True)
    submissions = [x for x in submissions if user_not_in_reviewers(x, user)]

    if len(submissions) > 0:
        todays_mwe = get_todays_mwe(user.language)
        submission = submissions[0]

        submission_category_messages = {
            "together": get_language_token(user.language, Token.FORM_SPECIAL_MEANING_TOGETHER) % todays_mwe.lemmas,
            "separated": get_language_token(user.language, Token.ARE_WORDS_SEPARATED) % todays_mwe.lemmas,
            "non-mwe": get_language_token(user.language, Token.DOESNT_FORM_SPECIAL_MEANING_TOGETHER) % todays_mwe.lemmas
        }

        if submission.category == SubmissionCategory.POSITIVE_TOGETHER or \
            submission.category == SubmissionCategory.POSITIVE_SEPARATED:
            reply_message = get_language_token(user.language, Token.REVIEW_QUESTION_POSITIVE) % (submission.value, submission.mwe_words)
            reply_to(user, update, reply_message)

    #     context.user_data["state"] = "review"
    #     context.user_data['submission'] = submission

    #     reply_message = get_language_token(user.language, Token.REVIEW_MESSAGE) % (submission.value, submission_category_messages[submission.category])
    #     update.message.reply_text(reply_message,
    #                               parse_mode=telegram.ParseMode.MARKDOWN,
    #                               reply_markup=get_review_type_keyboard_keyboard_markup(user.language))
    # else:
    #     if "state" in context.user_data:
    #         del context.user_data["state"]
    #     update.message.reply_text(
    #         get_language_token(user.language, Token.NO_EXAMPLES_TO_REVIEW),
    #         parse_mode=telegram.ParseMode.MARKDOWN,
    #         reply_markup=Keyboard.main(user.language)
    #     )
