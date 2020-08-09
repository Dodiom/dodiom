from database import session
from models import User, Submission, ReviewCategory, Review


def add_review(user: User, submission: Submission,
               category: ReviewCategory) -> Review:
    if user == submission.user:
        raise Exception("Review and submission user cannot be the same")
    review = Review(
        user=user,
        submission=submission,
        review_type=category,
        mwe=submission.mwe
    )
    if category == ReviewCategory.LIKE:
        submission.user.score_today += submission.points
        submission.user.score += submission.points
    user.score_today += 1
    user.score += 1
    session.add(review)
    session.commit()
    return review
