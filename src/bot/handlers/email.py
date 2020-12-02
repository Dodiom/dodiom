import re
import time

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from api.user import update_user
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.state_helper import set_state, State, clear_state
from bot.helpers.user_helper import reply_to, reply_html, get_user_from_update
from i18n import Token
from log import mwelog
from models import User


def main_email_handler(user: User, update: Update, context: CallbackContext):
    set_state(context, State.ADDING_EMAIL)

    if "sub_state" not in context.user_data:
        ask_for_email(user, update, context)
    else:
        sub_state = context.user_data["sub_state"]
        if sub_state == "typing_email":
            check_email_and_ask_confirmation(user, update, context)
        elif sub_state == "confirming_email":
            confirm_email(user, update, context)


def email_handler(update: Update, context: CallbackContext):
    user = get_user_from_update(update)
    main_email_handler(user, update, context)


def ask_for_email(user: User, update: Update, context: CallbackContext):
    mwelog.info(f"Asked for email from {user.username}")
    context.user_data["sub_state"] = "typing_email"
    reply_html(user, update, user.language.get(Token.ADD_EMAIL_START),
               reply_markup=Keyboard.remove())


def check_email_and_ask_confirmation(user: User, update: Update, context: CallbackContext):
    email_regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    email = update.message.text
    mwelog.info(f"Email got from {user.username}: {email}")
    if not re.match(email_regex, email):
        reply_to(user, update, user.language.get(Token.INVALID_EMAIL),
                 reply_markup=Keyboard.remove())
    else:
        context.user_data["sub_state"] = "confirming_email"
        context.user_data["email"] = email
        reply_html(user, update, user.language.get(Token.CONFIRM_EMAIL) % email,
                   reply_markup=Keyboard.email_verify_keyboard(user.language))


def confirm_email(user: User, update: Update, context: CallbackContext):
    available_inputs = [
        user.language.get(Token.YES),
        user.language.get(Token.NO),
        user.language.get(Token.CANCEL)
    ]

    message = update.message.text

    if message not in available_inputs:
        reply_to(user, update, user.language.get(Token.ENTER_VALID_COMMAND),
                 reply_markup=Keyboard.email_verify_keyboard(user.language))
        return

    if message == user.language.get(Token.YES):
        email = context.user_data["email"]
        user.email = email
        update_user(user)
        _clear_context(context)
        reply_html(user, update, user.language.get(Token.EMAIL_SET) % email,
                   Keyboard.main(user))
        mwelog.info(f"{user.username} confirms {email} is correct")
    else:
        _clear_context(context)
        reply_to(user, update, user.language.get(Token.EMAIL_CANCELLED),
                 Keyboard.main(user))


def _clear_context(context: CallbackContext):
    clear_state(context)
    if "sub_state" in context.user_data:
        del context.user_data["sub_state"]
    if "email" in context.user_data:
        del context.user_data["email"]


email_command_handler = CommandHandler(['eposta_ekle', 'add_email'], email_handler, run_async=True)
