from typing import List

import telegram
from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.keyboard_helper import Keyboard
from database import session
from i18n import Token, Language
from models import User


def scoreboard_handler(user: User, update: Update, context: CallbackContext):
    #  send_feedback_url_to_user(user, update)
    send_scoreboard_to_user(user, update)


def send_scoreboard_to_user(user: User, update: Update):
    if user.language == Language.ENGLISH:
        send_scoreboard_for_en(user, update)
    elif user.language == Language.TURKISH:
        send_scoreboard_for_tr(user, update)


def send_scoreboard_for_en(user: User, update: Update):
    users_sorted_by_score: List[User] = session\
        .query(User)\
        .filter(User.score_today_en > 0)\
        .order_by(User.score_today_en.desc())\
        .all()

    if len(users_sorted_by_score) > 0:
        scoreboard_message = user.language.get(Token.TOP_FIVE_USERS)
        user_appeared_in_first_five = False
        for i in range(0, 5):
            if i >= len(users_sorted_by_score):
                break
            rankings = ["🥇", "🥈", "🥉", "4\.", "5\."]
            username = users_sorted_by_score[i].username
            if user.id == users_sorted_by_score[i].id:
                username = "*%s* \(%s\)" % (username, user.language.get(Token.YOU))
                user_appeared_in_first_five = True
            ranking = rankings[i]
            if user.id == users_sorted_by_score[i].id:
                ranking = "*%s*" % ranking
            point = users_sorted_by_score[i].score_today_en
            scoreboard_message += "%s %s \- %d" % (ranking, username, point) + "\n"

        if not user_appeared_in_first_five:
            for i in range(len(users_sorted_by_score)):
                if users_sorted_by_score[i].id == user.id:
                    scoreboard_message += "\.\.\.\n"
                    scoreboard_message += "%d\. %s \- %d" % (
                        i + 1, user.username, users_sorted_by_score[i].score_today_en) + "\n"

        update.message.reply_text(
            scoreboard_message,
            parse_mode=telegram.ParseMode.MARKDOWN_V2,
            reply_markup=Keyboard.main(user.language)
        )
    else:
        update.message.reply_text(
            user.language.get(Token.NO_SUBMISSIONS),
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_markup=Keyboard.main(user.language)
        )


def send_scoreboard_for_tr(user: User, update: Update):
    users_sorted_by_score: List[User] = session\
        .query(User)\
        .filter(User.score_today_tr > 0)\
        .order_by(User.score_today_tr.desc())\
        .all()

    if len(users_sorted_by_score) > 0:
        scoreboard_message = user.language.get(Token.TOP_FIVE_USERS)
        user_appeared_in_first_five = False
        for i in range(0, 5):
            if i >= len(users_sorted_by_score):
                break
            rankings = ["🥇", "🥈", "🥉", "4\.", "5\."]
            username = users_sorted_by_score[i].username
            if user.id == users_sorted_by_score[i].id:
                username = "*%s* \(*__%s__*\)" % (username, user.language.get(Token.YOU))
                user_appeared_in_first_five = True
            ranking = rankings[i]
            if user.id == users_sorted_by_score[i].id:
                ranking = "*%s*" % ranking
            point = users_sorted_by_score[i].score_today_tr
            scoreboard_message += "%s %s \- %d" % (ranking, username, point) + "\n"

        if not user_appeared_in_first_five:
            for i in range(len(users_sorted_by_score)):
                if users_sorted_by_score[i].id == user.id:
                    scoreboard_message += "\.\.\.\n"
                    scoreboard_message += "%d\. %s \- %d" % (
                        i + 1, user.username, users_sorted_by_score[i].score_today_tr) + "\n"

        update.message.reply_text(
            scoreboard_message,
            parse_mode=telegram.ParseMode.MARKDOWN_V2,
            reply_markup=Keyboard.main(user.language)
        )
    else:
        update.message.reply_text(
            user.language.get(Token.NO_SUBMISSIONS),
            parse_mode=telegram.ParseMode.MARKDOWN,
            reply_markup=Keyboard.main(user.language)
        )
