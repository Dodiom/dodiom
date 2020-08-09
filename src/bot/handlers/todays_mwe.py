import logging

from telegram import Update

from bot.helpers.keyboard_helper import Keyboard
from api.mwe import get_todays_mwe
from bot.helpers.user_helper import reply_to
from i18n import Token, get_language_token
from models import User


def todays_mwe_handler(user: User, update: Update):
    logging.info("User {user_name} requested todays mwe.",
                 user_name=user.username, user_id=user.id)
    todays_mwe = get_todays_mwe(user.language)
    reply_to(user, update, get_language_token(user.language, Token.TODAYS_MWE_REPLY_TEXT) % (todays_mwe.name, todays_mwe.meaning),
             reply_markup=Keyboard.main(user.language))

