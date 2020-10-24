from telegram.ext import CallbackContext

from api.user import get_user
from database import database
from models import User, Submission


def flag_submission(user: User, submission_id: int, context: CallbackContext):
    if user.id == 1065263859:
        session = database.get_session()
        submission = session.query(Submission).filter(Submission.id == submission_id).first()
        submission.flagged = True
        database.commit(session)
        context.bot.send_message(user.id, f"Submission {submission_id} is flagged.")


def ban_user(user: User, user_id: int, context: CallbackContext):
    if user.id == 1065263859:
        session = database.get_session()
        banned_user = get_user(user_id)
        banned_user.banned = True
        for submission in session.query(Submission).filter(Submission.user == banned_user).all():
            submission.flagged = True
        database.commit()
        context.bot.send_message(user.id, f"User {user_id} is banned.")
