from datetime import datetime

from telegram import Update

from database import database
from i18n import Token
from models import FeedbackData, User


def create_feedback_data_for_user(user: User) -> FeedbackData:
    data = FeedbackData()
    data.user = user
    data.review_count = len(user.reviews)
    data.submission_count = len(user.submissions)
    data.created = datetime.now()
    session = database.get_session()
    try:
        session.add(data)
        session.commit()
        return data
    except:
        session.rollback()
        raise


def send_feedback_url_to_user(user: User, update: Update):
    feedback_data = create_feedback_data_for_user(user)
    update.message.reply_text(user.language.get(Token.FEEDBACK_MESSAGE))
    update.message.reply_text(user.language.get(Token.FEEDBACK_URL) % feedback_data.id)
