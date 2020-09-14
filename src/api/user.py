from typing import List
from datetime import datetime

from i18n import Language
from models import User
from database import session


def add_user(name: str, language: Language) -> User:
    user = User(
        username=name,
        language=language,
        viewed_help=False,
        score=0.0,
        score_today_en=0.0,
        score_today_tr=0.0,
        muted=False,
        created=datetime.now()
    )
    session.add(user)
    session.commit()
    return user


def add_user_with_id(uid: int, name: str, language: Language) -> User:
    user = User(
        id=uid,
        username=name,
        language=language,
        viewed_help=False,
        score=0.0,
        score_today_en=0.0,
        score_today_tr=0.0,
        muted=False,
        created=datetime.now()
    )
    session.add(user)
    session.commit()
    return user


def get_user(uid: int) -> User:
    return session.query(User).filter(User.id == uid).first()


def get_all_users() -> List[User]:
    return session.query(User).all()


def mute_user(uid: int) -> None:
    user = get_user(uid)
    user.muted = True
    session.commit()


def unmute_user(uid: int) -> None:
    user = get_user(uid)
    user.muted = False
    session.commit()
