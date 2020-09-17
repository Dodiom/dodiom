from sqlalchemy import func
from telegram import Update

from api.mwe import get_todays_mwe
from api.submission import get_category_score
from database import session
from i18n import Token
from models import SubmissionCategory, User, Mwe, Submission


def send_i_need_submission_category_message(user: User, update: Update, category: SubmissionCategory = None) -> None:
    todays_mwe = get_todays_mwe(user.language)
    submissions_category_counts = [
        [SubmissionCategory.POSITIVE_TOGETHER,
         _get_submission_category_count(todays_mwe, SubmissionCategory.POSITIVE_TOGETHER)],
        [SubmissionCategory.POSITIVE_SEPARATED,
         _get_submission_category_count(todays_mwe, SubmissionCategory.POSITIVE_SEPARATED)],
        [SubmissionCategory.NEGATIVE_TOGETHER,
         _get_submission_category_count(todays_mwe, SubmissionCategory.NEGATIVE_TOGETHER)],
        [SubmissionCategory.NEGATIVE_SEPARATED,
         _get_submission_category_count(todays_mwe, SubmissionCategory.NEGATIVE_SEPARATED)]
    ]

    if category is not None:
        submissions_category_counts = [x for x in submissions_category_counts if x[0] != category]

    submissions_category_counts.sort(key=lambda x: x[1])
    min_category = submissions_category_counts[0][0]

    category_messages = {
        SubmissionCategory.POSITIVE_TOGETHER: user.language.get(Token.I_NEED_PT_EXAMPLES),
        SubmissionCategory.POSITIVE_SEPARATED: user.language.get(Token.I_NEED_PS_EXAMPLES),
        SubmissionCategory.NEGATIVE_TOGETHER: user.language.get(Token.I_NEED_NT_EXAMPLES),
        SubmissionCategory.NEGATIVE_SEPARATED: user.language.get(Token.I_NEED_NS_EXAMPLES)
    }

    category_scores = {
        SubmissionCategory.POSITIVE_TOGETHER: get_category_score(user.language, SubmissionCategory.POSITIVE_TOGETHER, todays_mwe),
        SubmissionCategory.POSITIVE_SEPARATED: get_category_score(user.language, SubmissionCategory.POSITIVE_SEPARATED, todays_mwe),
        SubmissionCategory.NEGATIVE_TOGETHER: get_category_score(user.language, SubmissionCategory.NEGATIVE_TOGETHER, todays_mwe),
        SubmissionCategory.NEGATIVE_SEPARATED: get_category_score(user.language, SubmissionCategory.NEGATIVE_SEPARATED, todays_mwe)
    }

    update.message.reply_html(category_messages[min_category] % category_scores[min_category])


def _get_submission_category_count(mwe: Mwe, category: SubmissionCategory) -> int:
    return session.query(func.count(Submission.category))\
        .filter(Submission.mwe == mwe)\
        .filter(Submission.category == category)\
        .all()[0][0]
