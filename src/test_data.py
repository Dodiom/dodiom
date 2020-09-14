from api.user import add_user
from api.mwe import get_todays_mwe
from api.submission import add_submission_using_text
from api.review import add_review
from database import database
from i18n import Language
from models import ReviewCategory


def load_test_data() -> None:
    database.reset_database()

    todays_mwe_en = get_todays_mwe(Language.ENGLISH)

    jake = add_user("jake", Language.ENGLISH)
    amy = add_user("amy", Language.ENGLISH)
    boyle = add_user("boyle", Language.ENGLISH)

    sub1 = add_submission_using_text(jake, "I give up.", todays_mwe_en, [1, 2],
                                     True)
    sub2 = add_submission_using_text(amy,
                                     "I didn't know giving up was that easy...",
                                     todays_mwe_en, [4, 5], True)
    sub3 = add_submission_using_text(boyle, "Can you give that pencil up here?",
                                     todays_mwe_en, [2, 5], False)
    sub4 = add_submission_using_text(jake, "I don't know, should we just"
                                           " give up, what gives?",
                                     todays_mwe_en, [8, 9], True)

    re1 = add_review(boyle, sub1, ReviewCategory.LIKE)
    add_review(boyle, sub2, ReviewCategory.DISLIKE)
    add_review(jake, sub2, ReviewCategory.SKIP)
