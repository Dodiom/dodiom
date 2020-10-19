import logging

from telegram import ParseMode, Update
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.handlers.achievements import achievements_handler
from bot.handlers.feedback import feedback_handler
from bot.handlers.help import help_handler
from bot.handlers.language import language_change_handler, language_update_handler
from bot.handlers.review import main_review_handler
from bot.handlers.scoreboard import scoreboard_handler
from bot.handlers.submit import main_submit_handler, submission_contains_todays_mwe
from bot.handlers.todays_mwe import todays_mwe_handler
from bot.helpers.general import send_typing_action
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.state_helper import State, get_state
from bot.helpers.user_helper import get_user_from_update
from i18n import Token


@send_typing_action
def message(update: Update, context: CallbackContext):
    user = get_user_from_update(update)
    try:
        logging.info("New message from {user_name}: {message}",
                     user_name=user.username, message=update.message.text)

        if get_state(context) != State.NONE:
            state = get_state(context)
            logging.info("Current state for {user_name}: {state}",
                         user_name=user.username, state=str(state))
            if state == State.SUBMISSION:
                main_submit_handler(user, update, context)
            elif state == State.CHANGING_LANGUAGE:
                language_update_handler(user, update, context)
            elif state == State.REVIEWING:
                main_review_handler(user, update, context)
        else:
            if update.message.text == user.language.get(Token.TODAYS_MWE):
                todays_mwe_handler(user, update)
            elif update.message.text == user.language.get(Token.SUBMIT):
                main_submit_handler(user, update, context)
            elif update.message.text == user.language.get(Token.CHANGE_LANGUAGE):
                language_change_handler(user, update, context)
            elif update.message.text == user.language.get(Token.HELP):
                help_handler(user, update, context)
            elif update.message.text == user.language.get(Token.REVIEW):
                main_review_handler(user, update, context)
            elif update.message.text == user.language.get(Token.FEEDBACK):
                feedback_handler(user, update, context)
            elif update.message.text == user.language.get(Token.SHOW_SCOREBOARD):
                scoreboard_handler(user, update, context)
            elif update.message.text == user.language.get(Token.ACHIEVEMENTS):
                achievements_handler(user, update, context)
            elif submission_contains_todays_mwe(user, update.message.text):
                context.user_data["sub_state"] = "typing_example"
                main_submit_handler(user, update, context)
            else:
                update.message.reply_text(
                    user.language.get(Token.ENTER_VALID_COMMAND),
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=Keyboard.main(user.language)
                )
                context.bot.send_photo(user.id, open("assets/keyboard_button.png", "rb"))
                update.message.reply_text(
                         user.language.get(Token.WELCOME_MESSAGE_8),
                         parse_mode=ParseMode.MARKDOWN,
                         reply_markup=Keyboard.main(user.language))

    except Exception as ex:
        logging.error(f"erroneous message: {user.username}: {update.message.text}")
        logging.exception(str(ex))
        update.message.reply_text(user.language.get(Token.ERROR_OCCURRED))


message_handler = MessageHandler(Filters.text, message, run_async=True)


def sticker(update: Update, context: CallbackContext):
    logging.info("Got sticker: {sticker_id}", sticker_id=update.message.sticker.file_id)
    context.bot.send_sticker(update.effective_chat.id, update.message.sticker.file_id)


sticker_handler = MessageHandler(Filters.sticker, sticker, run_async=True)
