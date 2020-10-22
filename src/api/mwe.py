from datetime import date, datetime
from functools import lru_cache
from typing import List

from sqlalchemy import and_

from i18n import Language
from database import database
from models import Mwe, MweCategory


@lru_cache(maxsize=None)
def get_date_mwe(language: Language, day: date):
    session = database.get_session()
    mwe: Mwe = session.query(Mwe) \
        .filter(and_(Mwe.date == day, Mwe.language == language)) \
        .first()
    return mwe


def get_todays_mwe(language: Language) -> Mwe:
    return get_date_mwe(language, datetime.now().date())


def add_mwe(name: str, meaning: str,  language: Language, date: date,
            lemmas: List[str], category: MweCategory,
            verb_indices: List[bool]) -> None:
    session = database.get_session()
    mwe = Mwe(name=name,
              meaning=meaning,
              language=language,
              date=date,
              lemmas=lemmas,
              category=category)
    session.add(mwe)
    database.commit(session)
