from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.state_helper import clear_state, State, set_state
from bot.helpers.user_helper import reply_to
from database import database
from i18n import Token, Language
from log import mwelog
from models import User


def language_change_handler(user: User, update: Update, context: CallbackContext) -> None:
    mwelog.info("User {user_name} is changing language, current language: {language}",
                user_name=user.username, user_id=user.id, language=str(user.language))
    set_state(context, State.CHANGING_LANGUAGE)
    reply_to(user, update,
             user.language.get(Token.SELECT_LANGUAGE),
             Keyboard.language_selection(user.language))


def change_user_language(user: User, language: Language) -> None:
    session = database.get_session()
    user.language = language
    database.commit(session)
    mwelog.info("User {user_name} changed language to: {language}",
                user_name=user.username, user_id=user.id, language=str(user.language))


def language_update_handler(user: User, update: Update, context: CallbackContext) -> None:
    if update.message.text == user.language.get(Token.LANGUAGE_ENGLISH):
        change_user_language(user, Language.ENGLISH)
        clear_state(context)
        reply_to(user, update,
                 user.language.get(Token.LANGUAGE_CHANGE_SUCCESSFUL),
                 Keyboard.main(user.language))
    elif update.message.text == user.language.get(Token.LANGUAGE_TURKISH):
        change_user_language(user, Language.TURKISH)
        clear_state(context)
        reply_to(user, update,
                 user.language.get(Token.LANGUAGE_CHANGE_SUCCESSFUL),
                 Keyboard.main(user.language))
    else:
        mwelog.info("User {user_name} entered wrong value ({message}) for language change.",
                     user_name=user.username, user_id=user.id, message=update.message.text)
        reply_to(user, update,
                 user.language.get(Token.PLEASE_SELECT_VALID_LANGUAGE),
                 Keyboard.language_selection(user.language))
