from i18n import Language
from models import User
from database import session


def add_user(name: str, language: Language) -> User:
    user = User(
        username=name,
        language=language,
        viewed_help=False
    )
    session.add(user)
    session.commit()
    return user


def get_user(uid: str) -> User:
    return session.query(User).filter(User.id == uid).first()
