from datetime import datetime
from typing import List
import hashlib

from stanza import Document

from i18n import Language
from models import User, Submission, Mwe, SubmissionCategory
from database import session
from nlp import cupt
from nlp.language_helper import lowercase
from nlp.stanza import process_sentence


def add_submission_using_doc(user: User, doc: Document, mwe: Mwe,
                             mwe_indices: List[int],
                             positive: bool) -> Submission:
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

    submission_points = get_category_score(
        user.language,
        submission_category,
        mwe
    )

    submission_lemmas = [lowercase(x.lemma, user.language) for x in doc.iter_words()]
    submission_words = [x.text for x in doc.iter_words()]

    submission = Submission(
        value=doc.text,
        lemmas=submission_lemmas,
        words=submission_words,
        language=user.language,
        points=submission_points,
        score=0.0,
        category=submission_category,
        mwe=mwe,
        user=user,
        mwe_words=[submission_words[x] for x in mwe_indices],
        mwe_indices=mwe_indices,
        conllu=cupt.doc_to_cupt(doc, mwe.id, mwe.category, [x + 1 for x in mwe_indices]),
        hash=get_submission_hash(doc),
        created=datetime.now()
    )
    session.add(submission)
    session.commit()
    return submission


def add_submission_using_text(user: User, sentence: str, mwe: Mwe,
                              mwe_indices: List[int],
                              positive: bool) -> Submission:
    doc = process_sentence(user.language, sentence)
    return add_submission_using_doc(user, doc, mwe, mwe_indices, positive)


def get_category_score(language: Language, category: SubmissionCategory,
                       mwe: Mwe) -> float:
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


def get_submission_hash(doc: Document) -> str:
    submission_string = "".join([x.lemma for x in doc.iter_words() if x.pos != "PUNCT"])
    return hashlib.md5(submission_string.encode('utf-8')).hexdigest()
