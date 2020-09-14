import logging

from telegram import Update

from bot.helpers.keyboard_helper import Keyboard
from api.mwe import get_todays_mwe
from bot.helpers.time_helper import get_time_in_turkey
from bot.helpers.user_helper import reply_to
from i18n import Token, get_language_token
from models import User
from config import mwexpress_config


def todays_mwe_handler(user: User, update: Update):
    logging.info("User {user_name} requested todays mwe.",
                 user_name=user.username)
    turkey_time = get_time_in_turkey()
    if mwexpress_config.start_hour <= turkey_time.hour < mwexpress_config.end_hour:
        todays_mwe = get_todays_mwe(user.language)
        reply_to(user, update, get_language_token(user.language, Token.TODAYS_MWE_REPLY_TEXT) % (todays_mwe.name, todays_mwe.meaning),
                 reply_markup=Keyboard.main(user.language))
    else:
        reply_to(user, update, get_language_token(user.language, Token.GAME_HOURS_FINISHED) % mwexpress_config.start_hour,
                 reply_markup=Keyboard.main(user.language))
