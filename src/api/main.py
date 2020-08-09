from typing import List

from database import database
from i18n import Language
from models import User, Mwe


class MWExpressApi:
    def __init__(self):
        self.session = database.get_session()
        pass

    def add_user(self, name: str, language: Language) -> User:
        user = User(
            username=name,
            language=language,
            viewed_help=False,
            score=0.0,
            score_today=0.0
        )
        self.session.add(user)
        self.session.commit()
        return user

    def add_user_object(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        return user

    def get_user(self, uid: str) -> User:
        return self.session.query(User).filter(User.id == uid).first()


api = MWExpressApi()
