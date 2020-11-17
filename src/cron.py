import schedule
import time

from telegram import ParseMode

from api.achievements import award_achievement
from api.mwe import get_todays_mwe
from api.user import get_all_users, get_user
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.scoreboard import scoreboard
from bot.helpers.submission_scores import submission_scores
from bot.helpers.user_helper import send_message_to_user
from bot.stickers import GOOD_MORNING_STICKER, ACHIEVEMENT_STICKER
from config import mwexpress_config
from bot.main import mwexpress_bot
from i18n import Token, Language
from database import database
from log import mwelog
from models import AchievementType


def send_game_starting_message_to_all() -> None:
    mwelog.info("Sending game started message to all users")
    unmute_everyone()
    all_users = get_all_users()
    for user in all_users:
        try:
            mwexpress_bot.bot.send_sticker(user.id, GOOD_MORNING_STICKER)
            send_message_to_user(mwexpress_bot.bot, user,
                                 user.language.get(Token.GAME_STARTED))
            todays_mwe = get_todays_mwe(user.language)
            send_message_to_user(mwexpress_bot.bot, user,
                                 user.language.get(Token.TODAYS_MWE_REPLY_TEXT) % (todays_mwe.name, todays_mwe.meaning),
                                 reply_markup=Keyboard.main(user.language),
                                 parse_mode=ParseMode.HTML)
            time.sleep(0.3)
        except Exception as ex:
            mwelog.exception(str(ex))

    mwelog.info("Sent game started message to all users")


def end_of_day_job():
    award_champion()
    clear_scores_for_today()
    submission_scores.clear()


def award_champion():
    mwelog.info("Awarding champion")
    boards = scoreboard.scoreboards
    for language in Language.ENGLISH, Language.TURKISH, Language.ITALIAN:
        if len(boards[language]) > 0:
            first_user = get_user(boards[language][0].user_id)
            mwelog.info("{username} is the champion", username=first_user.username)
            award_achievement(first_user, AchievementType.CHAMPION)
            try:
                mwexpress_bot.bot.send_sticker(first_user.id, ACHIEVEMENT_STICKER)
                send_message_to_user(mwexpress_bot.bot, first_user,
                                     first_user.language.get(Token.CHAMPION_ACH_CONGRATS_MSG),
                                     parse_mode=ParseMode.HTML)
            except Exception as ex:
                mwelog.exception(ex)


def clear_scores_for_today():
    mwelog.info("Clearing scores for today")
    all_users = get_all_users()
    for user in all_users:
        user.score_today_en = 0
        user.score_today_tr = 0
        user.score_today_it = 0
    session = database.get_session()
    database.commit(session)
    scoreboard.iterate()


def unmute_everyone():
    mwelog.info("Unmuting everyone")
    all_users = get_all_users()
    for user in all_users:
        user.muted = False
    session = database.get_session()
    database.commit(session)


def schedule_jobs():
    pass
    # schedule.every().day.at(mwexpress_config.start_time.strftime("%H:%M"))\
    #     .do(send_game_starting_message_to_all)
    # schedule.every().day.at(mwexpress_config.end_time.strftime("%H:%M"))\
    #     .do(end_of_day_job)


def run_scheduled_jobs():
    while True:
        schedule.run_pending()
        time.sleep(2)
