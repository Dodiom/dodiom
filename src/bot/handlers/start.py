import logging

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from bot.helpers.state_helper import clear_state
from bot.helpers.user_helper import get_user_from_update, reply_to
from i18n import get_language_token, Token
from bot.helpers.keyboard_helper import Keyboard


def start(update: Update, context: CallbackContext):
    user = get_user_from_update(update)

    logging.info("User {user_name} started using Mwexpress",
                 user_name=user.username, user_id=user.id)

    clear_state(context)

    reply_to(user, update,
             get_language_token(user.language, Token.WELCOME_MESSAGE) % user.username,
             Keyboard.main(user.language))


start_handler = CommandHandler('start', start)
