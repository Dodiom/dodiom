from datetime import datetime
from typing import List

from sqlalchemy import func, and_
from telegram import Update
from telegram.ext import CallbackContext

from api.achievements import get_user_achievements
from database import database
from i18n import Token
from models import User, AchievementType, Submission, Review


def achievements_handler(user: User, update: Update, context: CallbackContext):
    session = database.get_session()
    level, next_threshold = get_level(user.score)
    update.message.reply_html(user.language.get(Token.LEVEL_MESSAGE) % (user.score, level, next_threshold))

    today = datetime.now().date()
    user_submission_count_today = session.query(Submission)\
        .filter(and_(Submission.user == user, func.Date(Submission.created) == today))\
        .count()
    user_review_count_today = session.query(Review) \
        .filter(and_(Review.user == user, func.Date(Review.created) == today)) \
        .count()
    update.message.reply_html(user.language.get(
        Token.USER_DAILY_PLAY_DETAILS_MESSAGE) % (
            user_submission_count_today, user_review_count_today
        )
    )

    user_achievements = get_user_achievements(user)

    update.message.reply_html(user.language.get(Token.UNLOCKED_ACHIEVEMENTS)
                              + "\n" + print_unlocked_achievements(user, user_achievements))

    update.message.reply_html(user.language.get(Token.LOCKED_ACHIEVEMENTS)
                              + "\n" + print_locked_achievements(user, user_achievements))

    if user.became_champion and user.email is None:
        update.message.reply_text(user.language.get(Token.CHAMP_BUT_NO_EMAIL))


def print_unlocked_achievements(user: User, achievements: List[AchievementType]) -> str:
    unlocked_message = ""
    if AchievementType.FIRST_SUBMISSION in achievements:
        unlocked_message += f'🏆 🌅 <b><u>{user.language.get(Token.FIRST_SUB_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.FIRST_SUB_ACH_DESC)}</i>\n'
    if AchievementType.EARLY_BIRD in achievements:
        unlocked_message += f'🏆 🐦 <b><u>{user.language.get(Token.EARLY_BIRD_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.EARLY_BIRD_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_1 in achievements:
        unlocked_message += f'🏆 🎇 <b><u>{user.language.get(Token.SUB_LVL_1_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.SUB_LVL_1_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_2 in achievements:
        unlocked_message += f'🏆 ✍️ <b><u>{user.language.get(Token.SUB_LVL_2_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.SUB_LVL_2_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_3 in achievements:
        unlocked_message += f'🏆 🗿 <b><u>{user.language.get(Token.SUB_LVL_3_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.SUB_LVL_3_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_4 in achievements:
        unlocked_message += f'🏆 📚 <b><u>{user.language.get(Token.SUB_LVL_4_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.SUB_LVL_4_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_5 in achievements:
        unlocked_message += f'🏆 🦄 <b><u>{user.language.get(Token.SUB_LVL_5_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.SUB_LVL_5_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_1 in achievements:
        unlocked_message += f'🏆 🤝 <b><u>{user.language.get(Token.REVIEW_LVL_1_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_1_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_2 in achievements:
        unlocked_message += f'🏆 🗳️ <b><u>{user.language.get(Token.REVIEW_LVL_2_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_2_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_3 in achievements:
        unlocked_message += f'🏆 ✨ <b><u>{user.language.get(Token.REVIEW_LVL_3_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_3_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_4 in achievements:
        unlocked_message += f'🏆 🧑‍🍳 <b><u>{user.language.get(Token.REVIEW_LVL_4_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_4_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_5 in achievements:
        unlocked_message += f'🏆 🕶️ <b><u>{user.language.get(Token.REVIEW_LVL_5_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_5_ACH_DESC)}</i>\n'
    if AchievementType.BECOME_NUMBER_ONE in achievements:
        unlocked_message += f'🏆 🥇 <b><u>{user.language.get(Token.BECOME_NUMBER_ONE_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.BECOME_NUMBER_ONE_ACH_DESC)}</i>\n'
    if AchievementType.CHAMPION in achievements:
        unlocked_message += f'🏆 🎖️ <b><u>{user.language.get(Token.CHAMPION_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.CHAMPION_ACH_DESC)}</i>\n'
    return unlocked_message


def print_locked_achievements(user: User, achievements: List[AchievementType]) -> str:
    locked_message = ""
    if AchievementType.FIRST_SUBMISSION not in achievements:
        locked_message += f'🌅 <b><u>{user.language.get(Token.FIRST_SUB_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.FIRST_SUB_ACH_DESC)}</i>\n'
    if AchievementType.EARLY_BIRD not in achievements:
        locked_message += f'🐦 <b><u>{user.language.get(Token.EARLY_BIRD_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.EARLY_BIRD_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_1 not in achievements:
        locked_message += f'🎇 <b><u>{user.language.get(Token.SUB_LVL_1_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.SUB_LVL_1_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_2 not in achievements:
        locked_message += f'✍️ <b><u>{user.language.get(Token.SUB_LVL_2_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.SUB_LVL_2_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_3 not in achievements:
        locked_message += f'🗿 <b><u>{user.language.get(Token.SUB_LVL_3_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.SUB_LVL_3_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_4 not in achievements:
        locked_message += f'📚 <b><u>{user.language.get(Token.SUB_LVL_4_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.SUB_LVL_4_ACH_DESC)}</i>\n'
    if AchievementType.SUB_LVL_5 not in achievements:
        locked_message += f'🦄 <b><u>{user.language.get(Token.SUB_LVL_5_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.SUB_LVL_5_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_1 not in achievements:
        locked_message += f'🤝 <b><u>{user.language.get(Token.REVIEW_LVL_1_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_1_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_2 not in achievements:
        locked_message += f'🗳️ <b><u>{user.language.get(Token.REVIEW_LVL_2_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_2_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_3 not in achievements:
        locked_message += f'✨ <b><u>{user.language.get(Token.REVIEW_LVL_3_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_3_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_4 not in achievements:
        locked_message += f'🧑‍🍳 <b><u>{user.language.get(Token.REVIEW_LVL_4_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_4_ACH_DESC)}</i>\n'
    if AchievementType.REVIEW_LVL_5 not in achievements:
        locked_message += f'🕶️ <b><u>{user.language.get(Token.REVIEW_LVL_5_ACH_NAME)}' \
                          f'</u></b>: <i>{user.language.get(Token.REVIEW_LVL_5_ACH_DESC)}</i>\n'
    if AchievementType.BECOME_NUMBER_ONE not in achievements:
        locked_message += f'🥇 <b><u>{user.language.get(Token.BECOME_NUMBER_ONE_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.BECOME_NUMBER_ONE_ACH_DESC)}</i>\n'
    if AchievementType.CHAMPION not in achievements:
        locked_message += f'🎖️ <b><u>{user.language.get(Token.CHAMPION_ACH_NAME)}' \
                            f'</u></b>: <i>{user.language.get(Token.CHAMPION_ACH_DESC)}</i>\n'
    return locked_message


def get_level(score: float) -> (int, int):
    if score <= 0:
        return 1, 1
    else:
        level = 0
        while True:
            if round((500 * (level ** 2) - (500 * level)) / 4) > score:
                break
            level += 1
        return level - 1, round((500 * (level ** 2) - (500 * level)) / 4)
