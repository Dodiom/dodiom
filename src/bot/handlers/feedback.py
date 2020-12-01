from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.user_helper import reply_to
from i18n import Token
from models import User


def feedback_handler(user: User, update: Update, context: CallbackContext) -> None:
    reply_to(user, update,
             user.language.get(Token.FEEDBACK_MESSAGE),
             Keyboard.main(user))
    reply_to(user, update,
             user.language.get(Token.FEEDBACK_URL),
             Keyboard.main(user))
