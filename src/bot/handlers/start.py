import logging
import time

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler

from bot.helpers.state_helper import clear_state
from bot.helpers.user_helper import get_user_from_update, reply_to
from i18n import Token
from bot.helpers.keyboard_helper import Keyboard


def start(update: Update, context: CallbackContext):
    user = get_user_from_update(update)

    logging.info("User {user_name} started using Mwexpress",
                 user_name=user.username, user_id=user.id)

    clear_state(context)

    context.bot.send_sticker(update.effective_chat.id,
                             "CAACAgIAAxkBAAIJbl9hsMfM-cDdZePry73czl7hs2KUAAKbAQACusCVBZcJB3MLKGZWGwQ")
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_1),
             Keyboard.main(user.language))
    time.sleep(0.5)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_2),
             Keyboard.main(user.language))
    time.sleep(0.5)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_3),
             Keyboard.main(user.language))
    time.sleep(0.5)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_4),
             Keyboard.main(user.language))
    time.sleep(0.5)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_5),
             Keyboard.main(user.language))
    time.sleep(0.5)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_6),
             Keyboard.main(user.language))
    time.sleep(0.5)
    update.message.reply_text(
        text=user.language.get(Token.WELCOME_MESSAGE_7),
        parse_mode=ParseMode.HTML,
        reply_markup=Keyboard.main(user.language))
    time.sleep(0.5)
    context.bot.send_photo(user.id, open("assets/keyboard_button.png", "rb"))
    time.sleep(0.5)
    reply_to(user, update,
             user.language.get(Token.WELCOME_MESSAGE_8),
             Keyboard.main(user.language))


start_handler = CommandHandler('start', start)
