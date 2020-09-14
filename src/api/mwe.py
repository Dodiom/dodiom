import logging
from datetime import date
from typing import List

from sqlalchemy import and_

from i18n import Language
from database import database
from models import Mwe, MweCategory
from bot.helpers.time_helper import get_time_in_turkey


def get_todays_mwe(language: Language) -> Mwe:
    turkey_time = get_time_in_turkey()
    turkey_date = date(turkey_time.year, turkey_time.month, turkey_time.day)
    session = database.get_session()
    logging.info("Todays MWE for language {language} is requested", language=str(language))
    mwe: Mwe = session.query(Mwe) \
        .filter(and_(Mwe.date == turkey_date, Mwe.language == language)) \
        .first()
    logging.info("{mwe} returned for todays MWE.", mwe=mwe.name)
    return mwe


def add_mwe(name: str, meaning: str,  language: Language, date: date,
            lemmas: List[str], category: MweCategory) -> None:
    session = database.get_session()
    mwe = Mwe(name=name,
              meaning=meaning,
              language=language,
              date=date,
              lemmas=lemmas,
              category=category)
    session.add(mwe)
    session.commit()
