from datetime import datetime

from bot.helpers.submission_scores import submission_scores
from i18n import Language
from models import User, Submission, Mwe, SubmissionCategory
from database import database
from nlp.parser import Parsed


def add_submission(user: User, parsed: Parsed, mwe: Mwe, positive: bool) -> Submission:
    mwe_indices = parsed.get_mwe_indices(mwe)
    sorted_mwe_indices = sorted(mwe_indices)
    together = all(y - x == 1 for x, y in zip(sorted_mwe_indices, sorted_mwe_indices[1:]))
    if together and positive:
        submission_category = SubmissionCategory.POSITIVE_TOGETHER
    elif not together and positive:
        submission_category = SubmissionCategory.POSITIVE_SEPARATED
    elif together and not positive:
        submission_category = SubmissionCategory.NEGATIVE_TOGETHER
    else:
        submission_category = SubmissionCategory.NEGATIVE_SEPARATED

    # submission_points = get_category_score(
    #     user.language,
    #     submission_category,
    #     mwe
    # )
    submission_points = submission_scores.get_category_score(submission_category,
                                                             user.language)

    submission = Submission(
        value=parsed.text,
        lemmas=parsed.lemmas,
        words=parsed.tokens,
        language=user.language,
        points=submission_points,
        score=0.0,
        category=submission_category,
        mwe=mwe,
        user=user,
        mwe_words=parsed.get_mwe_tokens(mwe),
        mwe_indices=list(mwe_indices),
        conllu="",
        hash="",
        created=datetime.now()
    )
    session = database.get_session()
    session.add(submission)
    database.commit(session)
    return submission


def get_category_score(language: Language, category: SubmissionCategory,
                       mwe: Mwe) -> float:
    session = database.get_session()
    all_submissions_count = session \
        .query(Submission) \
        .filter(Submission.language == language) \
        .filter(Submission.category == category) \
        .filter(Submission.mwe == mwe) \
        .count()
    category_initial_points = {
        SubmissionCategory.POSITIVE_TOGETHER: 10,
        SubmissionCategory.POSITIVE_SEPARATED: 20,
        SubmissionCategory.NEGATIVE_TOGETHER: 40,
        SubmissionCategory.NEGATIVE_SEPARATED: 30
    }
    score = round(_compound_interest(
        category_initial_points[category],
        -0.02,
        all_submissions_count
    ))
    return score if score > 0 else 1


def _compound_interest(p: int, r: float, n: float) -> float:
    return p * ((1 + r) ** n)
