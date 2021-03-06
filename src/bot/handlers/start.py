import time

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler

from bot.helpers.state_helper import clear_state
from bot.helpers.user_helper import get_user_from_update, reply_to
from bot.stickers import TIPS_FEDORA_STICKER
from i18n import Token
from bot.helpers.keyboard_helper import Keyboard
from log import mwelog


def start(update: Update, context: CallbackContext):
    user = get_user_from_update(update)

    mwelog.info("User {user_name} started using Mwexpress",
                user_name=user.username, user_id=user.id)

    clear_state(context)

    context.bot.send_sticker(update.effective_chat.id, TIPS_FEDORA_STICKER)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_1),
             Keyboard.remove())
    time.sleep(2)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_2),
             Keyboard.remove())
    time.sleep(5)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_3),
             Keyboard.remove())
    time.sleep(3)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_4),
             Keyboard.remove())
    time.sleep(2)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_5),
             Keyboard.remove())
    time.sleep(5)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_6),
             Keyboard.remove())
    time.sleep(10)
    update.message.reply_text(
        text=user.language.get(Token.WELCOME_MESSAGE_7),
        parse_mode=ParseMode.HTML,
        reply_markup=Keyboard.remove())
    time.sleep(5)
    context.bot.send_photo(user.id, open("assets/keyboard_button.png", "rb"))
    time.sleep(0.5)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_8))
    time.sleep(5)
    reply_to(user, update,
             user.language.get(Token.DISCLAIMER),
             Keyboard.main(user))


start_handler = CommandHandler('start', start, run_async=True)
