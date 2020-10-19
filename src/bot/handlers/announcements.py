from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from api.user import get_all_users
from bot.helpers.user_helper import send_message_to_user


def stats(update: Update, context: CallbackContext):
    message = update.message.text.replace("/announce ", "")
    if len(message) > 10:
        for user in get_all_users():
            send_message_to_user(context.bot, user, message)


announcements_handler = CommandHandler('announce', stats, run_async=True)
