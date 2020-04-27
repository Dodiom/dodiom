import logging

from telegram import ParseMode, Update
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.handlers.help import help_handler
from bot.handlers.language import language_change_handler, language_update_handler
from bot.handlers.submit import submit_handler, submit_category_handler, submit_message_handler
from bot.handlers.todays_mwe import todays_mwe_handler
from bot.helpers.general import send_typing_action
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.state_helper import State, get_state
from bot.helpers.user_helper import get_user_from_update
from i18n import get_language_token, Token


@send_typing_action
def message(update: Update, context: CallbackContext):
    try:
        user = get_user_from_update(update)
        logging.info("New message from {user_name}: {message}",
                     user_name=user.username, user_id=user.id,
                     message=update.message.text)

        if get_state(context) != State.NONE:
            state = get_state(context)
            logging.info("Current state for {user_name}: {state}",
                         user_name=user.username, user_id=user.id,
                         state=str(state))
            if state == State.TYPING_EXAMPLE:
                submit_message_handler(user, update, context)
            elif state == State.CHOOSING_SUBMISSION_CATEGORY:
                submit_category_handler(user, update, context)
            elif state == State.CHANGING_LANGUAGE:
                language_update_handler(user, update, context)
        else:
            logging.info("State is clear for {user_name}.",
                         user_name=user.username, user_id=user.id)
            if update.message.text == get_language_token(user.language, Token.TODAYS_MWE):
                todays_mwe_handler(user, update)
            elif update.message.text == get_language_token(user.language, Token.SUBMIT):
                submit_handler(user, update, context)
            elif update.message.text == get_language_token(user.language, Token.CHANGE_LANGUAGE):
                language_change_handler(user, update, context)
            elif update.message.text == get_language_token(user.language, Token.HELP):
                help_handler(user, update)
            else:
                update.message.reply_text(
                    get_language_token(user.language, Token.ENTER_VALID_COMMAND),
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=Keyboard.main(user.language)
                )

    except Exception as ex:
        logging.error(str(ex))
        update.message.reply_text(str(ex))


message_handler = MessageHandler(Filters.text, message)
