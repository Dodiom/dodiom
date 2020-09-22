import logging
from datetime import date, datetime
from typing import List

from sqlalchemy import and_

from i18n import Language
from database import database
from models import Mwe, MweCategory


def get_todays_mwe(language: Language) -> Mwe:
    session = database.get_session()
    logging.info("Todays MWE for language {language} is requested", language=str(language))
    mwe: Mwe = session.query(Mwe) \
        .filter(and_(Mwe.date == datetime.now().date(), Mwe.language == language)) \
        .first()
    logging.info("{mwe} returned for todays MWE.", mwe=mwe.name)
    return mwe


def add_mwe(name: str, meaning: str,  language: Language, date: date,
            lemmas: List[str], category: MweCategory,
            verb_indices: List[bool]) -> None:
    session = database.get_session()
    mwe = Mwe(name=name,
              meaning=meaning,
              language=language,
              date=date,
              lemmas=lemmas,
              category=category,
              verb_indices=verb_indices)
    session.add(mwe)
    session.commit()
