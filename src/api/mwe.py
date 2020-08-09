import logging
from datetime import date

from i18n import Language
from database import database
from models import Mwe, MweCategory


def get_todays_mwe(language: Language) -> Mwe:
    session = database.get_session()
    logging.info("Todays MWE for language {language} is requested", language=str(language))
    if language == Language.ENGLISH:
        mwe: Mwe = session.query(Mwe).filter(Mwe.name == "(to) give up").first()

        if mwe is None:
            mwe = Mwe(name="(to) give up",
                      meaning="cease making an effort; admit defeat",
                      language=Language.ENGLISH,
                      date=date(2020, 3, 28),
                      lemmas=["give", "up"],
                      category=MweCategory.VPC)
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
                      lemmas=["ayva", "ye"],
                      category=MweCategory.VID)
            session.add(mwe)
            session.commit()

        logging.info("{mwe} returned for todays MWE.", mwe=mwe.name)
        return mwe
