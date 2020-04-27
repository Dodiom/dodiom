import logging
from datetime import date

from database import session
from i18n import Language
from models import Mwe


def get_todays_mwe(language: Language) -> Mwe:
    logging.info("Todays MWE for language {language} is requested", language=str(language))
    if language == Language.ENGLISH:
        mwe: Mwe = session.query(Mwe).filter(Mwe.name == "(to) give up").first()

        if mwe is None:
            mwe = Mwe(name="(to) give up",
                      meaning="cease making an effort; admit defeat",
                      language=Language.ENGLISH,
                      date=date(2020, 3, 28),
                      lemmas=["give", "up"])
            session.add(mwe)
            session.commit()

        logging.info("{mwe} returned for todays MWE.", mwe=mwe.name)
        return mwe
    elif language == Language.TURKISH:
        mwe: Mwe = session.query(Mwe).filter(Mwe.name == "ayvayı yemek").first()

        if mwe is None:
            mwe = Mwe(name="ayvayı yemek",
                      meaning="kötü bir duruma düşmek",
                      language=Language.TURKISH,
                      date=date(2020, 3, 28),
                      lemmas=["ayva", "ye"])
            session.add(mwe)
            session.commit()

        logging.info("{mwe} returned for todays MWE.", mwe=mwe.name)
        return mwe
