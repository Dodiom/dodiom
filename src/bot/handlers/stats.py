import logging
import statistics
from datetime import datetime

from sqlalchemy import func
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from api.user import get_all_users
from bot.helpers.user_helper import get_user_from_update, send_message_to_user
from database import session
from i18n import Token
from models import User, Submission, Review


def stats(update: Update, context: CallbackContext):
    for user in get_all_users():
        send_message_to_user(context.bot, user,
                             "Merhabalar, sistemsel kaynaklı sıkıntılar nedeniyle oyuna kısa bir süre ara veriyoruz. 😥 Sorun çözüldüğünde kaldığımız yerden devam edeceğiz.")

    user = get_user_from_update(update)
    logging.info(f"Stats requested by {user.username}")

    today = datetime.now().date()

    if len(context.args) == 3:
        day = int(context.args[0])
        month = int(context.args[1])
        year = int(context.args[2])
        today = datetime(year, month, day).date()

    update.message.reply_text(f'Stats for {today.strftime("%A, %B %d, %Y")}')

    all_users_count = session.query(User).filter(func.Date(User.created) <= today).count()
    new_users = session.query(User).filter(func.Date(User.created) == today).all()
    update.message.reply_text(f'{all_users_count} users (+{len(new_users)} new)')
    if len(new_users) > 0:
        update.message.reply_text(f'New users: {", ".join([x.username for x in new_users])}')

    all_submissions_count = session.query(Submission).filter(func.Date(Submission.created) <= today).count()
    new_submissions_count = session.query(Submission).filter(func.Date(Submission.created) == today).count()
    update.message.reply_text(f'{all_submissions_count} submissions (+{new_submissions_count} new)')

    all_reviews_count = session.query(Review).filter(func.Date(Review.created) <= today).count()
    new_reviews_count = session.query(Review).filter(func.Date(Review.created) == today).count()
    update.message.reply_text(f'{all_reviews_count} reviews (+{new_reviews_count} new)')

    all_subs = session.query(Submission).all()
    all_subs_today = session.query(Submission).filter(func.Date(Submission.created) == today).all()
    review_count_average = round(statistics.mean([x.review_count for x in all_subs]), 2)
    review_count_average_today = 0.0
    if len(all_subs_today) > 0:
        review_count_average_today = round(statistics.mean([x.review_count for x in all_subs_today]), 2)
    update.message.reply_text(f'Review count average: {review_count_average}({review_count_average_today} today)')

    all_reviews_today = session.query(Review).filter(func.Date(Review.created) == today).all()
    all_submitted_users_today = set([x.user.id for x in all_subs_today])
    all_reviewed_users_today = set([x.user.id for x in all_reviews_today])

    update.message.reply_text(f'Users who only submitted: {len([x for x in all_submitted_users_today if x not in all_reviewed_users_today])}')
    update.message.reply_text(f'Users who only reviewed: {len([x for x in all_reviewed_users_today if x not in all_submitted_users_today])}')
    update.message.reply_text(f'Users who both submitted and reviewed: {len([x for x in all_submitted_users_today if x in all_reviewed_users_today])}')


stats_handler = CommandHandler('stats', stats, run_async=True)
