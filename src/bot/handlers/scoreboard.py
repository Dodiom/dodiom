from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.scoreboard import scoreboard
from models import User


def scoreboard_handler(user: User, update: Update, context: CallbackContext):
    scoreboard.send_to_user(user, update)
