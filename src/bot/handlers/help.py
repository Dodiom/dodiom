from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.user_helper import reply_to
from bot.stickers import TIPS_FEDORA_STICKER
from database import database
from i18n import Token
from models import User


def help_handler(user: User, update: Update, context: CallbackContext) -> None:
    context.bot.send_sticker(update.effective_chat.id, TIPS_FEDORA_STICKER)
    session = database.get_session()
    if not user.viewed_help:
        user.viewed_help = True
        database.commit(session)
    reply_to(user, update,
             user.language.get(Token.HELP_MESSAGE),
             Keyboard.main(user.language))
    reply_to(user, update,
             user.language.get(Token.DISCLAIMER),
             Keyboard.main(user.language))
