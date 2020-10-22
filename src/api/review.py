from datetime import datetime

from database import database
from i18n import Language
from models import User, Submission, ReviewCategory, Review


def add_review(user: User, submission: Submission,
               category: ReviewCategory) -> Review:
    if user == submission.user:
        raise Exception("Review and submission user cannot be the same")
    review = Review(
        user=user,
        submission=submission,
        review_type=category,
        mwe=submission.mwe,
        created=datetime.now()
    )
    if category == ReviewCategory.LIKE:
        if submission.language == Language.ENGLISH:
            submission.user.score_today_en += submission.points
            user.score_today_en += 1
        elif submission.language == Language.TURKISH:
            submission.user.score_today_tr += submission.points
            user.score_today_tr += 1
        submission.user.score += submission.points
        submission.score += submission.points
    user.score += 1
    session = database.get_session()
    session.add(review)
    database.commit(session)
    return review
