from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from api.user import get_all_users
from bot.helpers.notification_manager import notification_manager
from bot.helpers.submission_scores import submission_scores
from bot.helpers.user_helper import send_message_to_user, get_user_from_update


def stats(update: Update, context: CallbackContext):
    message = update.message.text.replace("/announce ", "")
    if len(message) > 10:
        for user in get_all_users():
            send_message_to_user(context.bot, user, message)


announcements_handler = CommandHandler('announce', stats, run_async=True)


def review_happy_hour(update: Update, context: CallbackContext):
    user = get_user_from_update(update)
    if user.id == 1065263859 or user.id == 1036601606:
        notification_manager.send_review_worth_more(context)
        submission_scores.start_review_happy_hour()


review_happy_hour_handler = CommandHandler('reviewhappyhour', review_happy_hour, run_async=True)
