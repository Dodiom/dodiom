import random

from sqlalchemy import func
from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.submission_scores import submission_scores
from database import database
from i18n import Token
from models import SubmissionCategory, User, Mwe, Submission


def _get_submission_category_count(mwe: Mwe, category: SubmissionCategory) -> int:
    session = database.get_session()
    return session.query(func.count(Submission.category))\
        .filter(Submission.mwe == mwe)\
        .filter(Submission.category == category)\
        .all()[0][0]


def send_hint_message(user: User, update: Update, context: CallbackContext):
    choices = [2, 3]
    if submission_scores.buffed_category[user.language] == SubmissionCategory.POSITIVE_TOGETHER:
        choices.append(4)
    elif submission_scores.buffed_category[user.language] == SubmissionCategory.NEGATIVE_TOGETHER:
        choices.append(1)
    choice = random.choice(choices)
    if choice == 1:
        update.message.reply_html(user.language.get(Token.HINT_MESSAGE_1))
    elif choice == 2:
        update.message.reply_text(user.language.get(Token.HINT_MESSAGE_2))
    elif choice == 3:
        update.message.reply_html(user.language.get(Token.HINT_MESSAGE_3))
    elif choice == 4:
        update.message.reply_text(user.language.get(Token.HINT_MESSAGE_4))
