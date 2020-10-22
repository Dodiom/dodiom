from typing import List
from datetime import datetime

from i18n import Language
from models import User
from database import database


def add_user(name: str, language: Language) -> User:
    user = User(
        username=name,
        language=language,
        viewed_help=False,
        viewed_todays_mwe_help=False,
        viewed_submission_help=False,
        viewed_review_help=False,
        score=0.0,
        score_today_en=0.0,
        score_today_tr=0.0,
        muted=False,
        created=datetime.now()
    )
    session = database.get_session()
    session.add(user)
    database.commit(session)
    return user


def add_user_with_id(uid: int, name: str, language: Language) -> User:
    user = User(
        id=uid,
        username=name,
        language=language,
        viewed_help=False,
        viewed_todays_mwe_help=False,
        viewed_submission_help=False,
        viewed_review_help=False,
        score=0.0,
        score_today_en=0.0,
        score_today_tr=0.0,
        muted=False,
        created=datetime.now()
    )
    session = database.get_session()
    session.add(user)
    database.commit(session)
    return user


def get_user(uid: int) -> User:
    session = database.get_session()
    return session.query(User).filter(User.id == uid).first()


def get_all_users() -> List[User]:
    session = database.get_session()
    return session.query(User).all()


def mute_user(uid: int) -> None:
    session = database.get_session()
    user = get_user(uid)
    user.muted = True
    database.commit(session)


def unmute_user(uid: int) -> None:
    session = database.get_session()
    user = get_user(uid)
    user.muted = False
    database.commit(session)


def update_user(user: User) -> None:
    database.commit(database.get_session())
