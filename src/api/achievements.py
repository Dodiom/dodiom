from sqlalchemy import and_

from database import database
from models import User, AchievementType, Achievement


def user_has_achievement(user: User, ach_type: AchievementType):
    session = database.get_session()
    return session.query(Achievement)\
        .filter(and_(Achievement.user == user, Achievement.type == ach_type))\
        .count() > 0


def award_achievement(user: User, ach_type: AchievementType):
    if not user_has_achievement(user, ach_type):
        session = database.get_session()
        achievement = Achievement(user=user, type=ach_type)
        session.add(achievement)
        database.commit(session)
