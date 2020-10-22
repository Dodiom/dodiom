from datetime import datetime
from typing import Optional, Dict

from sqlalchemy import func
from telegram import ParseMode
from telegram.ext import CallbackContext

from api.mwe import get_todays_mwe
from bot.helpers.scoreboard import scoreboard
from database import database
from i18n import Token, Language
from log import mwelog
from models import SubmissionCategory, Submission


class SubmissionScores:
    def __init__(self):
        self.buffed_category: Dict[Language, Optional[SubmissionCategory]] = {
            Language.ENGLISH: None,
            Language.TURKISH: None
        }
        self.iterate()

    def get_category_score(self, category: SubmissionCategory,
                           language: Language) -> int:
        if category == self.buffed_category[language]:
            return 15
        else:
            return 10

    def iterate(self, context: Optional[CallbackContext] = None):
        session = database.get_session()
        for language in Language.ENGLISH, Language.TURKISH:
            todays_mwe = get_todays_mwe(language)
            positive_together_count = session.query(Submission)\
                .filter(Submission.category == SubmissionCategory.POSITIVE_TOGETHER)\
                .filter(Submission.mwe == todays_mwe)\
                .count()
            positive_separated_count = session.query(Submission)\
                .filter(Submission.category == SubmissionCategory.POSITIVE_SEPARATED)\
                .filter(Submission.mwe == todays_mwe)\
                .count()
            negative_together_count = session.query(Submission)\
                .filter(Submission.category == SubmissionCategory.NEGATIVE_TOGETHER)\
                .filter(Submission.mwe == todays_mwe)\
                .count()
            negative_separated_count = session.query(Submission)\
                .filter(Submission.category == SubmissionCategory.NEGATIVE_SEPARATED)\
                .filter(Submission.mwe == todays_mwe)\
                .count()
            counts = {
                SubmissionCategory.POSITIVE_TOGETHER: positive_together_count,
                SubmissionCategory.POSITIVE_SEPARATED: positive_separated_count,
                SubmissionCategory.NEGATIVE_TOGETHER: negative_together_count,
                SubmissionCategory.NEGATIVE_SEPARATED: negative_separated_count,  # unimportant
            }
            counts_list = [positive_together_count, positive_separated_count, negative_together_count]
            if self.buffed_category[language] is None:
                if max(counts_list) - min(counts_list) >= 15:
                    if counts[SubmissionCategory.POSITIVE_SEPARATED] == min(counts_list):
                        self.buffed_category[language] = SubmissionCategory.POSITIVE_SEPARATED
                    elif counts[SubmissionCategory.POSITIVE_TOGETHER] == min(counts_list):
                        self.buffed_category[language] = SubmissionCategory.POSITIVE_TOGETHER
                    elif counts[SubmissionCategory.NEGATIVE_TOGETHER] == min(counts_list):
                        self.buffed_category[language] = SubmissionCategory.NEGATIVE_TOGETHER
                    notification_messages = {
                        SubmissionCategory.POSITIVE_TOGETHER: Token.POS_TOG_WORTH_MORE,
                        SubmissionCategory.POSITIVE_SEPARATED: Token.POS_SEP_WORTH_MORE,
                        SubmissionCategory.NEGATIVE_TOGETHER: Token.NEG_TOG_WORTH_MORE
                    }
                    if context is not None:
                        for score in scoreboard.scoreboards[language]:
                            try:
                                context.bot.send_message(score.user_id,
                                                         language.get(notification_messages[self.buffed_category[language]]),
                                                         parse_mode=ParseMode.HTML)
                            except Exception as ex:
                                mwelog.exception(str(ex))
            else:
                if abs(max(counts_list) - counts[self.buffed_category[language]]) < 10:
                    self.buffed_category[language] = None

    def clear(self):
        self.buffed_category = None


submission_scores = SubmissionScores()
