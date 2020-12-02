import time

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from api.user import get_all_users
from bot.helpers.notification_manager import notification_manager
from bot.helpers.submission_scores import submission_scores
from bot.helpers.user_helper import send_message_to_user, get_user_from_update
from bot.stickers import EXCITED_STICKER
from config import mwexpress_config
from i18n import Token
from log import mwelog


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


def send_i_need_x_examples(update: Update, context: CallbackContext):
    user = get_user_from_update(update)
    if user.id == 1065263859 or user.id == 1036601606:
        notification_manager.send_i_need_x_examples(context)


i_need_x_examples_handler = CommandHandler('sendhelp', send_i_need_x_examples, run_async=True)


def send_game_started_again_with_awards(update: Update, context: CallbackContext):
    mwelog.info("Sending game started again message to all users")
    user = get_user_from_update(update)
    if user.id == mwexpress_config.moderator or user.id == 1065263859:
        for user in get_all_users():
            try:
                mwelog.info(f"Sending game started again message to {user.username}")
                context.bot.send_sticker(user.id, EXCITED_STICKER)
                send_message_to_user(context.bot, user, user.language.get(Token.GAME_STARTED_AGAIN_ANNOUNCEMENT))
                time.sleep(0.5)
            except Exception as ex:
                mwelog.exception(str(ex))


game_started_again_handler = CommandHandler('game_started_again', send_game_started_again_with_awards, run_async=True)


def claim_email_announcement(update: Update, context: CallbackContext):
    mwelog.info("Sending claim email announcement to champions")
    user = get_user_from_update(update)
    if user.id == mwexpress_config.moderator or user.id == 1065263859:
        for user in get_all_users():
            if user.became_champion:
                try:
                    mwelog.info(f"Sending claim email message to {user.username}")
                    context.bot.send_sticker(user.id, EXCITED_STICKER)
                    context.bot.send_message(user.id, user.language.get(Token.CHAMP_BUT_NO_EMAIL))
                    time.sleep(0.5)
                except Exception as ex:
                    mwelog.exception(str(ex))


claim_email_command_handler = CommandHandler('claim_emails', claim_email_announcement, run_async=True)