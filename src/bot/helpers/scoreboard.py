from typing import List

import telegram
from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from api.achievements import user_has_achievement, award_achievement
from api.user import get_user
from bot.helpers.keyboard_helper import Keyboard
from bot.stickers import ACHIEVEMENT_STICKER, WORRIED_STICKER, EXCITED_STICKER
from database import database
from i18n import Language, Token
from models import User, AchievementType


class UserScore:
    def __init__(self, user_id: int, username: str, score: float):
        self.user_id = user_id
        self.username = username
        self.score = score

    def __repr__(self):
        return f"<Score({self.username};{self.score})>"

    def __str__(self):
        return self.__repr__()


class ScoreBoard:
    def __init__(self):
        self.scoreboards = {
            Language.TURKISH: self.get_scoreboard(Language.TURKISH),
            Language.ENGLISH: self.get_scoreboard(Language.ENGLISH)
        }
        self.old_scoreboards = self.scoreboards

    def iterate(self, update: Update, context: CallbackContext):
        new_boards = {
            Language.TURKISH: self.get_scoreboard(Language.TURKISH),
            Language.ENGLISH: self.get_scoreboard(Language.ENGLISH)
        }

        for language in Language.ENGLISH, Language.TURKISH:
            if len(new_boards[language]) > 0:
                first_user = get_user(new_boards[language][0].user_id)
                if not user_has_achievement(first_user, AchievementType.BECOME_NUMBER_ONE):
                    award_achievement(first_user, AchievementType.BECOME_NUMBER_ONE)
                    context.bot.send_sticker(first_user.id, ACHIEVEMENT_STICKER)
                    context.bot.send_message(first_user.id,
                                             first_user.language.get(Token.BECOME_NUMBER_ONE_ACH_CONGRATS_MSG),
                                             parse_mode=ParseMode.HTML)
                else:
                    context.bot.send_sticker(first_user.id, EXCITED_STICKER)
                    context.bot.send_message(first_user.id,
                                             first_user.language.get(Token.YOUVE_BECOME_LEADER))

            if len(new_boards[language]) > 5 and len(self.old_scoreboards[language]) > 4:
                if new_boards[language][5].user_id == self.old_scoreboards[language][4].user_id:
                    sixth_user = get_user(new_boards[language][5].user_id)
                    context.bot.send_sticker(sixth_user.id, WORRIED_STICKER)
                    context.bot.send_message(sixth_user.id, sixth_user.language.get(Token.LOST_FIRST_FIVE))

        self.old_scoreboards = self.scoreboards
        self.scoreboards = new_boards

    def send_to_user(self, user: User, update: Update):
        board = self.scoreboards[user.language]
        if len(board) > 0:
            scoreboard_message = user.language.get(Token.TOP_FIVE_USERS)
            user_appeared_in_first_five = False
            for i in range(0, 5):
                if i >= len(board):
                    break
                rankings = ["🥇", "🥈", "🥉", "4\.", "5\."]
                username = board[i].username
                if user.id == board[i].user_id:
                    username = "*%s* \(%s\)" % (username, user.language.get(Token.YOU))
                    user_appeared_in_first_five = True
                ranking = rankings[i]
                if user.id == board[i].user_id:
                    ranking = "*%s*" % ranking
                point = board[i].score
                change = ""
                old_ranking = self.get_old_ranking(board[i].user_id, user.language)
                if old_ranking > i:
                    change = "🔼 "
                elif old_ranking < i:
                    change = "🔻 "
                scoreboard_message += "%s %s%s \- %d" % (ranking, change, username, point) + "\n"

            if not user_appeared_in_first_five:
                for i in range(len(board)):
                    if board[i].user_id == user.id:
                        scoreboard_message += "\.\.\.\n"
                        scoreboard_message += "%d\. %s \- %d" % (
                            i + 1, user.username, board[i].score) + "\n"

            update.message.reply_text(
                scoreboard_message,
                parse_mode=telegram.ParseMode.MARKDOWN_V2,
                reply_markup=Keyboard.main(user.language)
            )
        else:
            update.message.reply_text(
                user.language.get(Token.SCOREBOARD_EMPTY),
                parse_mode=telegram.ParseMode.MARKDOWN,
                reply_markup=Keyboard.main(user.language)
            )

    def get_old_ranking(self, user_id: int, language: Language) -> int:
        for i in range(len(self.old_scoreboards[language])):
            if self.old_scoreboards[language][i].user_id == user_id:
                return i
        return 1000

    @staticmethod
    def get_scoreboard(language: Language) -> List[UserScore]:
        session = database.get_session()
        board = []
        if language == Language.TURKISH:
            users_sorted_by_score: List[User] = session \
                .query(User) \
                .filter(User.score_today_tr > 0) \
                .order_by(User.score_today_tr.desc()) \
                .all()
            for user in users_sorted_by_score:
                board.append(UserScore(user.id, user.username, user.score_today_tr))
        elif language == Language.ENGLISH:
            users_sorted_by_score: List[User] = session \
                .query(User) \
                .filter(User.score_today_en > 0) \
                .order_by(User.score_today_en.desc()) \
                .all()
            for user in users_sorted_by_score:
                board.append(UserScore(user.id, user.username, user.score_today_en))
        return board


scoreboard = ScoreBoard()
