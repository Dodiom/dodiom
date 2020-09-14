import logging

import schedule
import time

from api.mwe import get_todays_mwe
from api.user import get_all_users
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.user_helper import send_message_to_user
from config import mwexpress_config
from bot.main import mwexpress_bot
from i18n import Token
from database import session


def send_game_starting_message_to_all() -> None:
    all_users = get_all_users()
    for user in all_users:
        send_message_to_user(mwexpress_bot.bot, user,
                             user.language.get(Token.GAME_STARTED))
        todays_mwe = get_todays_mwe(user.language)
        send_message_to_user(mwexpress_bot.bot, user,
                             user.language.get(Token.TODAYS_MWE_REPLY_TEXT) % (todays_mwe.name, todays_mwe.meaning),
                             reply_markup=Keyboard.main(user.language))
    logging.info("Sent game started message to all users")


def send_game_over_message_to_all() -> None:
    all_users = get_all_users()
    for user in all_users:
        send_message_to_user(mwexpress_bot.bot, user,
                             user.language.get(Token.GAME_ENDED))
    print("hey")


def clear_scores_for_today():
    logging.info("Clearing scores for today")
    all_users = get_all_users()
    for user in all_users:
        user.score_today_en = 0
        user.score_today_tr = 0
    session.commit()


def schedule_jobs():
    schedule.every().day.at(f"{mwexpress_config.start_hour:02}:00").do(send_game_starting_message_to_all)
    schedule.every().day.at(f"{mwexpress_config.end_hour}:00").do(send_game_over_message_to_all)
    schedule.every().day.at("23:32").do(clear_scores_for_today)


def run_scheduled_jobs():
    while True:
        schedule.run_pending()
        time.sleep(2)
