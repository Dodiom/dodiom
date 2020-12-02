from telegram import Update
from telegram.ext import CallbackContext

from api.mwe import get_todays_mwe
from bot.helpers.scoreboard import scoreboard
from database import database
from i18n import Token
from models import User, Submission


def scoreboard_handler(user: User, update: Update, context: CallbackContext):
    scoreboard.send_to_user(user, update)
    todays_mwe = get_todays_mwe(user.language)
    session = database.get_session()
    submission_count_now = session.query(Submission).filter(Submission.mwe == todays_mwe).count()
    if submission_count_now < 100:
        update.message.reply_text(user.language.get(Token.TODAYS_TARGET) % (100 - submission_count_now))
    if user.became_champion and user.email is None:
        update.message.reply_text(user.language.get(Token.CHAMP_BUT_NO_EMAIL))
