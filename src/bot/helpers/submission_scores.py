from datetime import datetime, timedelta
from typing import Optional, Dict

from telegram.ext import CallbackContext

from api.mwe import get_todays_mwe
from bot.helpers.notification_manager import notification_manager
from database import database
from i18n import Language
from models import SubmissionCategory, Submission


class SubmissionScores:
    def __init__(self):
        self.buffed_category: Dict[Language, Optional[SubmissionCategory]] = {
            Language.ENGLISH: None,
            Language.TURKISH: None
        }
        self._review_happy_hour_start_time: Optional[datetime] = None
        self.iterate()

    def get_category_score(self, category: SubmissionCategory,
                           language: Language) -> int:
        if category == SubmissionCategory.POSITIVE_SEPARATED:
            if self.buffed_category[language] == SubmissionCategory.POSITIVE_TOGETHER:
                return 17
            else:
                return 12
        elif category == SubmissionCategory.NEGATIVE_SEPARATED:
            return 10
        if category == self.buffed_category[language]:
            return 15
        else:
            return 10

    def get_review_score(self) -> int:
        if self._review_happy_hour_start_time is not None:
            if datetime.now() > (self._review_happy_hour_start_time + timedelta(hours=1)):
                self._review_happy_hour_start_time = None
        if self._review_happy_hour_start_time is not None:
            return 2
        else:
            return 1

    def start_review_happy_hour(self):
        self._review_happy_hour_start_time = datetime.now()

    def iterate(self, context: Optional[CallbackContext] = None):
        session = database.get_session()
        for language in Language.ENGLISH, Language.TURKISH:
            todays_mwe = get_todays_mwe(language)
            positive_together_count = session.query(Submission)\
                .filter(Submission.category == SubmissionCategory.POSITIVE_TOGETHER)\
                .filter(Submission.mwe == todays_mwe)\
                .count()
            negative_together_count = session.query(Submission)\
                .filter(Submission.category == SubmissionCategory.NEGATIVE_TOGETHER)\
                .filter(Submission.mwe == todays_mwe)\
                .count()
            diff = abs(positive_together_count - negative_together_count)
            if self.buffed_category[language] is None:
                if diff >= 15:
                    if positive_together_count < negative_together_count:
                        self.buffed_category[language] = SubmissionCategory.POSITIVE_TOGETHER
                        notification_manager.send_idioms_worth_more(context)
                    else:
                        self.buffed_category[language] = SubmissionCategory.NEGATIVE_TOGETHER
                        notification_manager.send_non_idioms_worth_more(context)
            else:
                if diff < 10:
                    self.buffed_category[language] = None

    def clear(self):
        for language in Language.ENGLISH, Language.TURKISH:
            self.buffed_category[language] = None


submission_scores = SubmissionScores()
