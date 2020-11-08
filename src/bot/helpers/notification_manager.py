import time
from collections import defaultdict
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import List, Dict, Optional

from telegram import ParseMode
from telegram.ext import CallbackContext

from api.mwe import get_todays_mwe
from api.user import get_all_users
from bot.stickers import EXCITED_STICKER, THUMBS_UP_STICKER, SAD_FACEPALM_STICKER, SAD_RAIN_STICKER
from config import mwexpress_config
from database import database
from i18n import get_random_congrats_message, Token
from log import mwelog
from models import User, Submission


class NotificationType(Enum):
    SOMEONE_LIKED_YOUR_EXAMPLE = auto()
    IDIOM_WORTH_MORE = auto()
    NON_IDIOM_WORTH_MORE = auto()
    BECAME_FIRST = auto()
    LOST_FIRST_THREE = auto()
    LOST_FIRST_FIVE = auto()
    REVIEW_WORTH_MORE = auto()
    LOST_FIRST = auto()
    I_NEED_X_EXAMPLES = auto()

    def get_ttl(self) -> timedelta:
        if self == self.SOMEONE_LIKED_YOUR_EXAMPLE:
            return timedelta(minutes=5)
        elif self == self.IDIOM_WORTH_MORE or self == self.NON_IDIOM_WORTH_MORE:
            return timedelta(hours=2)
        elif self == self.BECAME_FIRST or self == self.LOST_FIRST_THREE \
                or self == self.LOST_FIRST_FIVE or self == self.LOST_FIRST:
            return timedelta(hours=2)
        elif self == self.REVIEW_WORTH_MORE:
            return timedelta(hours=1)
        else:
            return timedelta(hours=1)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class SentNotification:
    def __init__(self, user_id: int, not_type: NotificationType, issued: datetime):
        self.user_id = user_id
        self.not_type = not_type
        self.issued = issued

    def is_expired(self) -> bool:
        now = datetime.now()
        expiration = self.issued + self.not_type.get_ttl()
        print(f"now: {now}, issued: {self.issued}, expir: {expiration}")
        print(f"expired: {expiration > now}")
        return now > expiration

    def __repr__(self):
        return f"<Sent Notification({self.user_id};{self.not_type};{self.issued})>"


class NotificationManager:
    def __init__(self):
        self._notification_history: Dict[int, List[SentNotification]] = defaultdict(list)
        self._notifications_cleared = datetime.now()

    def _history_contains_notification(self, user_id: int, not_type: NotificationType):
        return any([x.not_type == not_type for x in self._notification_history[user_id]])

    def _clear_old_notifications(self):
        if (datetime.now() - self._notifications_cleared).seconds > 60:
            for user_id in self._notification_history.keys():
                self._notification_history[user_id] = [notification for notification
                                                       in self._notification_history[user_id]
                                                       if not notification.is_expired()]
            self._notifications_cleared = datetime.now()

    def send_someone_liked_your_example(self, user: User, context: CallbackContext):
        self._clear_old_notifications()
        if not user.muted:
            self._send_notification(context, user.id, user.language.get(Token.SOMEONE_LOVED_YOUR_EXAMPLE) %
                                    (get_random_congrats_message(user.language)),
                                    NotificationType.SOMEONE_LIKED_YOUR_EXAMPLE)

    def send_idioms_worth_more(self, context: CallbackContext):
        self._clear_old_notifications()
        for user in get_all_users():
            self._send_notification(context, user.id, user.language.get(Token.POS_TOG_WORTH_MORE),
                                    NotificationType.IDIOM_WORTH_MORE,
                                    THUMBS_UP_STICKER,
                                    ParseMode.HTML)
            time.sleep(0.3)

    def send_non_idioms_worth_more(self, context: CallbackContext):
        self._clear_old_notifications()
        for user in get_all_users():
            self._send_notification(context, user.id,
                                    user.language.get(Token.NEG_TOG_WORTH_MORE),
                                    NotificationType.NON_IDIOM_WORTH_MORE,
                                    THUMBS_UP_STICKER,
                                    ParseMode.HTML)
            time.sleep(0.3)

    def send_became_first(self, user: User, context: CallbackContext):
        self._clear_old_notifications()
        self._send_notification(context, user.id,
                                user.language.get(Token.YOUVE_BECOME_LEADER),
                                NotificationType.BECAME_FIRST, EXCITED_STICKER)

    def send_lost_three(self, user: User, context: CallbackContext):
        self._clear_old_notifications()
        self._send_notification(context, user.id,
                                user.language.get(Token.LOST_FIRST_THREE),
                                NotificationType.LOST_FIRST_THREE,
                                SAD_FACEPALM_STICKER)

    def send_lost_five(self, user: User, context: CallbackContext):
        self._clear_old_notifications()
        self._send_notification(context, user.id,
                                user.language.get(Token.LOST_FIRST_FIVE),
                                NotificationType.LOST_FIRST_FIVE,
                                SAD_FACEPALM_STICKER)

    def send_lost_first(self, user: User, context: CallbackContext):
        self._clear_old_notifications()
        self._send_notification(context, user.id,
                                user.language.get(Token.LOST_FIRST),
                                NotificationType.LOST_FIRST,
                                SAD_FACEPALM_STICKER)

    def send_review_worth_more(self, context: CallbackContext):
        self._clear_old_notifications()
        for user in get_all_users():
            self._send_notification(context, user.id,
                                    user.language.get(Token.REVIEW_WORTH_MORE),
                                    NotificationType.REVIEW_WORTH_MORE,
                                    THUMBS_UP_STICKER,
                                    ParseMode.HTML)
            time.sleep(0.3)

    def send_i_need_x_examples(self, context: CallbackContext):
        self._clear_old_notifications()
        language = mwexpress_config.language
        todays_mwe = get_todays_mwe(language)
        session = database.get_session()
        submission_count_now = session.query(Submission).filter(Submission.mwe == todays_mwe).count()
        if submission_count_now < 100:
            for user in get_all_users():
                self._send_notification(context, user.id,
                                        user.language.get(Token.TODAYS_TARGET) % (100 - submission_count_now),
                                        NotificationType.I_NEED_X_EXAMPLES,
                                        SAD_RAIN_STICKER)
                time.sleep(0.3)

    def _send_notification(self, context: CallbackContext, user_id: int,
                           message: str, not_type: NotificationType,
                           sticker: Optional[str] = None,
                           reply_markup: Optional[str] = None):
        if not self._history_contains_notification(user_id, not_type):
            try:
                mwelog.info("Sending {not_type} to {user_id}",
                            not_type=str(not_type), user_id=user_id)
                notification = SentNotification(user_id,
                                                not_type,
                                                datetime.now())
                self._notification_history[user_id].append(notification)
                if sticker is not None:
                    context.bot.send_sticker(user_id, sticker)
                context.bot.send_message(user_id, message, reply_markup=reply_markup)
            except Exception as ex:
                mwelog.exception(str(ex))


notification_manager = NotificationManager()
