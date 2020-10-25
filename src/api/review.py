from datetime import datetime

from bot.helpers.submission_scores import submission_scores
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
        elif submission.language == Language.TURKISH:
            submission.user.score_today_tr += submission.points
        submission.user.score += submission.points
        submission.score += submission.points
    user.score += submission_scores.get_review_score()
    if submission.language == Language.ENGLISH:
        user.score_today_en += submission_scores.get_review_score()
    elif submission.language == Language.TURKISH:
        user.score_today_tr += submission_scores.get_review_score()
    session = database.get_session()
    session.add(review)
    database.commit(session)
    return review
