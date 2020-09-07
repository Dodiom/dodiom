from typing import List

import telegram
from telegram import Update
from telegram.ext import CallbackContext

from bot.helpers.keyboard_helper import Keyboard
from database import session
from i18n import get_language_token, Token
from models import User


def scoreboard_handler(user: User, update: Update, context: CallbackContext):
    users_sorted_by_score: List[User] = \
        session.query(User).filter(User.language == user.language)\
        .order_by(User.score_today.desc()).all()

    if len(users_sorted_by_score) > 0:
        scoreboard_message = get_language_token(user.language, Token.TOP_FIVE_USERS)
        user_appeared_in_first_five = False
        for i in range(0, 5):
            if i >= len(users_sorted_by_score):
                break
            rankings = ["🥇", "🥈", "🥉", "4\.", "5\."]
            username = users_sorted_by_score[i].username
            if user.id == users_sorted_by_score[i].id:
                username = "*%s* \(%s\)" % (username, get_language_token(user.language, Token.YOU))
                user_appeared_in_first_five = True
            ranking = rankings[i]
            if user.id == users_sorted_by_score[i].id:
                ranking = "*%s*" % ranking
            point = users_sorted_by_score[i].score_today
            scoreboard_message += "%s %s \- %d" % (ranking, username, point) + "\n"

        if not user_appeared_in_first_five:
            for i in range(len(users_sorted_by_score)):
                if users_sorted_by_score[i].id == user.id:
                    scoreboard_message += "\.\.\.\n"
                    scoreboard_message += "%d\. %s \- %d" % (i + 1, user.username, users_sorted_by_score[i].score_today) + "\n"

        update.message.reply_text(
            scoreboard_message,
            parse_mode=telegram.ParseMode.MARKDOWN_V2,
            reply_markup=Keyboard.main(user.language)
        )
    else:
        update.message.reply_text(
            get_language_token(user.language, Token.NO_SUBMISSIONS),
            parse_mode=telegram.ParseMode.MARKDOWN_V2,
            reply_markup=Keyboard.main(user.language)
        )

    pass