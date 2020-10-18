import time
from datetime import datetime
from typing import List

from telegram import Update
from telegram.ext import CallbackContext

from api.mwe import get_todays_mwe
from api.user import unmute_user, mute_user, update_user
from bot.helpers.keyboard_helper import Keyboard
from bot.helpers.state_helper import set_state, State, clear_state
from bot.helpers.user_helper import reply_to, send_message_to_user, reply_html
from config import mwexpress_config
from database import session
from i18n import Token, get_random_congrats_message
from models import Submission, User, SubmissionCategory, ReviewCategory, Mwe
from api.review import add_review
from nlp.parsing import parser


def _user_not_in_reviewers(submission: Submission, user: User) -> bool:
    all_reviewer_names = [x.user.username for x in submission.reviews]
    return user.username not in all_reviewer_names


def get_submissions_to_review(mwe: Mwe, user: User) -> List[Submission]:
    submissions = session.query(Submission) \
        .filter(Submission.user != user) \
        .filter(Submission.mwe == mwe) \
        .filter(Submission.flagged == False) \
        .all()
    submissions = sorted(submissions, key=lambda x: x.review_count)
    return [x for x in submissions if _user_not_in_reviewers(x, user)]


def main_review_handler(user: User, update: Update, context: CallbackContext):
    now = datetime.now().time()
    if mwexpress_config.start_time <= now < mwexpress_config.end_time:
        set_state(context, State.REVIEWING)

        if "submission" in context.user_data:
            _review_answer_handler(user, update, context)
            return

        _send_submission_to_review(user, update, context)
    else:
        clear_state(context)
        unmute_user(user.id)
        _safe_delete_context_data(context, "submission")
        _safe_delete_context_data(context, "review_count")
        reply_to(user, update, user.language.get(Token.GAME_HOURS_FINISHED) % mwexpress_config.start_time.hour,
                 reply_markup=Keyboard.main(user.language))


def _send_submission_to_review(user: User, update: Update, context: CallbackContext):
    if not user.viewed_review_help:
        reply_to(user, update, user.language.get(Token.REVIEW_HELP_MESSAGE_1))
        time.sleep(4)
        reply_to(user, update, user.language.get(Token.REVIEW_HELP_MESSAGE_2))
        time.sleep(4)
        user.viewed_review_help = True
        update_user(user)

    todays_mwe = get_todays_mwe(user.language)
    submissions = get_submissions_to_review(todays_mwe, user)

    if len(submissions) > 0:
        submission: Submission = submissions[0]
        context.user_data["submission"] = submission
        if "review_count" not in context.user_data:
            context.user_data["review_count"] = 0

        parsed = parser.parse(submission.language, submission.value)
        review_example = submission.value
        for index in reversed(sorted(submission.mwe_indices)):
            start_index = parsed.token_positions[index][0]
            end_index = parsed.token_positions[index][1]
            review_example = review_example[:end_index] + "</u></b>" + review_example[end_index:]
            review_example = review_example[:start_index] + "<b><u>" + review_example[start_index:]

        if submission.category == SubmissionCategory.POSITIVE_SEPARATED or \
                submission.category == SubmissionCategory.POSITIVE_TOGETHER:
            review_question = user.language.get(Token.REVIEW_QUESTION_POSITIVE) \
                              % (review_example, _get_word_list_str_from_submission(submission))
            reply_html(user, update, review_question,
                       Keyboard.review_keyboard(user.language))
        else:
            review_question = user.language.get(Token.REVIEW_QUESTION_NEGATIVE) \
                              % (review_example, _get_word_list_str_from_submission(submission))
            reply_html(user, update, review_question,
                       Keyboard.review_keyboard(user.language))
    else:
        if "review_count" in context.user_data:
            reply_to(user, update, user.language.get(Token.NO_SUB_LEFT_TO_REVIEW),
                     Keyboard.main(user.language))
        else:
            reply_to(user, update, user.language.get(Token.NO_SUBMISSIONS),
                     Keyboard.main(user.language))
        clear_state(context)
        unmute_user(user.id)
        _safe_delete_context_data(context, "submission")
        _safe_delete_context_data(context, "review_count")


def _get_word_list_str_from_submission(submission: Submission):
    mwe_words = [f"<b><u>{x}</u></b>" for x in submission.mwe_words]
    first_ones = mwe_words[:-1]
    last_one = mwe_words[-1]
    return f'{", ".join(first_ones)} {submission.language.get(Token.AND)} {last_one}'


def _review_answer_handler(user: User, update: Update, context: CallbackContext):
    mute_user(user.id)
    available_inputs = [
        user.language.get(Token.AGREE_NICE_EXAMPLE),
        user.language.get(Token.DO_NOT_LIKE_EXAMPLE),
        user.language.get(Token.SKIP_THIS_ONE),
        user.language.get(Token.QUIT_REVIEWING)
    ]

    if update.message.text not in available_inputs:
        reply_to(user, update,
                 user.language.get(Token.PLEASE_ENTER_VALID_REVIEW),
                 Keyboard.review_keyboard(user.language))
        return

    submission = context.user_data["submission"]
    context.user_data["review_count"] += 1

    if update.message.text == user.language.get(Token.AGREE_NICE_EXAMPLE):
        add_review(user, submission, ReviewCategory.LIKE)
        reply_to(user, update,
                 user.language.get(Token.THANKS_FOR_REVIEW) % (get_random_congrats_message(user.language), 1))
        if not submission.user.muted:
            send_message_to_user(context.bot, submission.user,
                                 user.language.get(Token.SOMEONE_LOVED_YOUR_EXAMPLE) % (
                                 get_random_congrats_message(submission.user.language), submission.points))
    elif update.message.text == user.language.get(Token.DO_NOT_LIKE_EXAMPLE):
        add_review(user, submission, ReviewCategory.DISLIKE)
        reply_to(user, update,
                 user.language.get(Token.THANKS_FOR_REVIEW) % (get_random_congrats_message(user.language), 1))
    elif update.message.text == user.language.get(Token.SKIP_THIS_ONE):
        add_review(user, submission, ReviewCategory.SKIP)
    else:
        unmute_user(user.id)
        reply_to(user, update,
                 user.language.get(Token.REVIEW_CANCELLED),
                 Keyboard.main(user.language))
        _safe_delete_context_data(context, "submission")
        clear_state(context)
        return

    _send_submission_to_review(user, update, context)


def _safe_delete_context_data(context: CallbackContext, name: str) -> None:
    if name in context.user_data:
        del context.user_data[name]
