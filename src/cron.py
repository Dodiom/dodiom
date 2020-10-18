import logging

import schedule
import time

from telegram import ParseMode

from api.mwe import get_todays_mwe
from api.user import get_all_users
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.user_helper import send_message_to_user
from bot.stickers import GOOD_MORNING_STICKER, GOOD_NIGHT_STICKER
from config import mwexpress_config
from bot.main import mwexpress_bot
from i18n import Token
from database import session


def send_game_starting_message_to_all() -> None:
    unmute_everyone()
    all_users = get_all_users()
    for user in all_users:
        mwexpress_bot.bot.send_sticker(user.id, GOOD_MORNING_STICKER)
        send_message_to_user(mwexpress_bot.bot, user,
                             user.language.get(Token.GAME_STARTED))
        todays_mwe = get_todays_mwe(user.language)
        send_message_to_user(mwexpress_bot.bot, user,
                             user.language.get(Token.TODAYS_MWE_REPLY_TEXT) % (todays_mwe.name, todays_mwe.meaning),
                             reply_markup=Keyboard.main(user.language),
                             parse_mode=ParseMode.HTML)
    logging.info("Sent game started message to all users")


def send_game_over_message_to_all() -> None:
    unmute_everyone()
    all_users = get_all_users()
    clear_scores_for_today()
    for user in all_users:
        if user.score_today() > 0:
            mwexpress_bot.bot.send_sticker(user.id, GOOD_NIGHT_STICKER)
            send_message_to_user(mwexpress_bot.bot, user,
                                 user.language.get(Token.GAME_ENDED))


def clear_scores_for_today():
    logging.info("Clearing scores for today")
    all_users = get_all_users()
    for user in all_users:
        user.score_today_en = 0
        user.score_today_tr = 0
    session.commit()


def unmute_everyone():
    logging.info("Unmuting everyone")
    all_users = get_all_users()
    for user in all_users:
        user.muted = False
    session.commit()


def schedule_jobs():
    schedule.every().day.at(mwexpress_config.start_time.strftime("%H:%M"))\
        .do(send_game_starting_message_to_all)
    schedule.every().day.at(mwexpress_config.end_time.strftime("%H:%M"))\
        .do(send_game_over_message_to_all)


def run_scheduled_jobs():
    while True:
        schedule.run_pending()
        time.sleep(2)
