from datetime import datetime
import time

from telegram import Update, ParseMode

from api.user import update_user
from bot.helpers.keyboard_helper import Keyboard
from api.mwe import get_todays_mwe
from bot.helpers.submission_scores import submission_scores
from bot.helpers.user_helper import reply_to
from i18n import Token
from models import User, SubmissionCategory
from config import mwexpress_config


def todays_mwe_handler(user: User, update: Update):
    now = datetime.now().time()
    if mwexpress_config.start_time <= now <= mwexpress_config.end_time:
        todays_mwe = get_todays_mwe(user.language)
        update.message.reply_text(text=user.language.get(Token.TODAYS_MWE_REPLY_TEXT) % (todays_mwe.name, todays_mwe.meaning),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=Keyboard.main(user))
        if submission_scores.buffed_category[user.language] is not None:
            notification_messages = {
                SubmissionCategory.POSITIVE_TOGETHER: Token.POS_TOG_WORTH_MORE,
                SubmissionCategory.POSITIVE_SEPARATED: Token.POS_SEP_WORTH_MORE,
                SubmissionCategory.NEGATIVE_TOGETHER: Token.NEG_TOG_WORTH_MORE
            }
            update.message.reply_html(
                user.language.get(notification_messages[submission_scores.buffed_category[user.language]]))
        if not user.viewed_todays_mwe_help:
            time.sleep(3)
            update.message.reply_text(
                text=user.language.get(Token.TODAYS_MWE_HELP_MESSAGE_1),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=Keyboard.main(user))
            time.sleep(5)
            update.message.reply_text(
                text=user.language.get(Token.TODAYS_MWE_HELP_MESSAGE_2),
                parse_mode=ParseMode.HTML,
                reply_markup=Keyboard.main(user))
            user.viewed_todays_mwe_help = True
            update_user(user)
    else:
        reply_to(user, update, user.language.get(Token.GAME_HOURS_FINISHED) % mwexpress_config.start_time.hour,
                 reply_markup=Keyboard.main(user))
