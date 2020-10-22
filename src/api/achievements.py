from typing import List

from sqlalchemy import and_

from database import database
from models import User, AchievementType, Achievement


def get_user_achievements(user: User) -> List[AchievementType]:
    session = database.get_session()
    user_achievements = session.query(Achievement)\
        .filter(Achievement.user == user)\
        .all()
    achievements = []
    for achievement in user_achievements:
        achievements.append(achievement.type)
    return achievements


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
