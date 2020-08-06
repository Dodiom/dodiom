from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.user_helper import reply_to
from i18n import Token, get_language_token
from models import User


def feedback_handler(user: User, update: Update, context: CallbackContext) -> None:
    reply_to(user, update,
             get_language_token(user.language, Token.FEEDBACK_MESSAGE),
             Keyboard.main(user.language))
    reply_to(user, update,
             get_language_token(user.language, Token.FEEDBACK_URL),
             Keyboard.main(user.language))
