from api.main import api
from bot.helpers.mwe_helper import get_todays_mwe, get_mwe_lemma_locations
from database import database
from i18n import Language
from models import User, Submission
from bot.handlers.submit import create_submission_from_text, finalize_submission


def load_test_data() -> None:
    session = database.get_session()
    database.reset_database()

    todays_mwe_en = get_todays_mwe(Language.ENGLISH)

    jake = api.add_user("jake", Language.ENGLISH)
    amy = api.add_user("amy", Language.ENGLISH)
    boyle = api.add_user("boyle", Language.ENGLISH)

    sub1 = create_submission_from_text("I give up", todays_mwe_en, Language.ENGLISH)
    sub1.user = jake
    finalize_submission(sub1, True)

    session.add(sub1)
    session.commit()

    sub2 = create_submission_from_text("I didn't know giving up was that easy...", todays_mwe_en, Language.ENGLISH)
    sub2.user = amy
    finalize_submission(sub2, True)

    session.add(sub2)
    session.commit()

    sub3 = create_submission_from_text("Can you give that pencil up here?", todays_mwe_en, Language.ENGLISH)
    sub3.user = boyle
    finalize_submission(sub3, False)

    session.add(sub3)
    session.commit()

    sub4 = create_submission_from_text("I don't know, should we just give up, what gives?", todays_mwe_en, Language.ENGLISH)
    sub4.user = jake
    finalize_submission(sub4, True)


    xxx = get_mwe_lemma_locations("I don't know, should we just give up, what gives?", todays_mwe_en, Language.ENGLISH)

    session.add(sub4)
    session.commit()
