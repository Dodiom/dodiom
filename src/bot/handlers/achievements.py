from telegram import Update
from telegram.ext import CallbackContext

from api.achievements import user_has_achievement
from i18n import Token
from models import User, AchievementType


def achievements_handler(user: User, update: Update, context: CallbackContext):
    level, next_threshold = get_level(user.score)
    update.message.reply_html(user.language.get(Token.LEVEL_MESSAGE) % (user.score, level, next_threshold))

    update.message.reply_html(user.language.get(Token.UNLOCKED_ACHIEVEMENTS)
                              + "\n" + print_unlocked_achievements(user))

    update.message.reply_html(user.language.get(Token.LOCKED_ACHIEVEMENTS)
                              + "\n" + print_locked_achievements(user))


def print_unlocked_achievements(user: User) -> str:
    unlocked_message = ""
    if user_has_achievement(user, AchievementType.FIRST_SUBMISSION):
        unlocked_message += f'🏆 🌅 <b><u>{user.language.get(Token.FIRST_SUB_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.FIRST_SUB_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.EARLY_BIRD):
        unlocked_message += f'🏆 🐦 <b><u>{user.language.get(Token.EARLY_BIRD_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.EARLY_BIRD_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.SUB_LVL_1):
        unlocked_message += f'🏆 <b><u>{user.language.get(Token.SUB_LVL_1_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_1_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.SUB_LVL_2):
        unlocked_message += f'🏆 ✍️ <b><u>{user.language.get(Token.SUB_LVL_2_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_2_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.SUB_LVL_3):
        unlocked_message += f'🏆 <b><u>{user.language.get(Token.SUB_LVL_3_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_3_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.SUB_LVL_4):
        unlocked_message += f'🏆 📚 <b><u>{user.language.get(Token.SUB_LVL_4_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_4_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.SUB_LVL_5):
        unlocked_message += f'🏆 <b><u>{user.language.get(Token.SUB_LVL_5_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_5_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.REVIEW_LVL_1):
        unlocked_message += f'🏆 🤝 <b><u>{user.language.get(Token.REVIEW_LVL_1_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_1_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.REVIEW_LVL_2):
        unlocked_message += f'🏆 <b><u>{user.language.get(Token.REVIEW_LVL_2_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_2_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.REVIEW_LVL_3):
        unlocked_message += f'🏆 <b><u>{user.language.get(Token.REVIEW_LVL_3_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_3_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.REVIEW_LVL_4):
        unlocked_message += f'🏆 <b><u>{user.language.get(Token.REVIEW_LVL_4_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_4_ACH_DESC)}\n'
    if user_has_achievement(user, AchievementType.REVIEW_LVL_5):
        unlocked_message += f'🏆 <b><u>{user.language.get(Token.REVIEW_LVL_5_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_5_ACH_DESC)}\n'
    return unlocked_message


def print_locked_achievements(user: User) -> str:
    locked_message = ""
    if not user_has_achievement(user, AchievementType.FIRST_SUBMISSION):
        locked_message += f'🌅 <b><u>{user.language.get(Token.FIRST_SUB_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.FIRST_SUB_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.EARLY_BIRD):
        locked_message += f'🐦 <b><u>{user.language.get(Token.EARLY_BIRD_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.EARLY_BIRD_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.SUB_LVL_1):
        locked_message += f'<b><u>{user.language.get(Token.SUB_LVL_1_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_1_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.SUB_LVL_2):
        locked_message += f'✍️ <b><u>{user.language.get(Token.SUB_LVL_2_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_2_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.SUB_LVL_3):
        locked_message += f'<b><u>{user.language.get(Token.SUB_LVL_3_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_3_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.SUB_LVL_4):
        locked_message += f'📚 <b><u>{user.language.get(Token.SUB_LVL_4_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_4_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.SUB_LVL_5):
        locked_message += f'<b><u>{user.language.get(Token.SUB_LVL_5_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.SUB_LVL_5_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.REVIEW_LVL_1):
        locked_message += f'🤝 <b><u>{user.language.get(Token.REVIEW_LVL_1_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_1_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.REVIEW_LVL_2):
        locked_message += f'<b><u>{user.language.get(Token.REVIEW_LVL_2_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_2_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.REVIEW_LVL_3):
        locked_message += f'<b><u>{user.language.get(Token.REVIEW_LVL_3_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_3_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.REVIEW_LVL_4):
        locked_message += f'<b><u>{user.language.get(Token.REVIEW_LVL_4_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_4_ACH_DESC)}\n'
    if not user_has_achievement(user, AchievementType.REVIEW_LVL_5):
        locked_message += f'<b><u>{user.language.get(Token.REVIEW_LVL_5_ACH_NAME)}' \
                            f'</u></b>: {user.language.get(Token.REVIEW_LVL_5_ACH_DESC)}\n'
    return locked_message


def get_level(score: float) -> (int, int):
    if score <= 0:
        return 1
    else:
        level = 0
        while True:
            if round((500 * (level ** 2) - (500 * level)) / 4) > score:
                break
            level += 1
        return level - 1, round((500 * (level ** 2) - (500 * level)) / 4)
