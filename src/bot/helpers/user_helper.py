import logging
from typing import Optional

from telegram import Update, ParseMode, Bot, ReplyMarkup

from database import database
from i18n import Language
from models import User
from api.main import api


def get_user_from_update(update: Update) -> User:
    session = database.get_session()
    user = api.get_user(update.effective_user.id)

    if user is None:
        new_user = User(
            id=update.effective_user.id,
            username=update.effective_user.username,
            language=Language.ENGLISH,
            viewed_help=False)
        if new_user.username is None:
            new_user.username = str(new_user.id)
        return api.add_user_object(new_user)
    else:
        if (user.username == str(user.id) or user.username is None) and update.effective_user.username is not None:
            user.username = update.effective_user.username
            session.commit()

    return user


def send_message_to_user(bot: Bot, user: User, msg: str) -> None:
    bot.send_message(chat_id=user.id,
                     text=msg,
                     parse_mode=ParseMode.MARKDOWN)


def reply_to(user: User, update: Update, message: str,
             reply_markup: Optional[ReplyMarkup] = None) -> None:
    """
    Sends a reply back to user.

    :param user: User to reply to
    :param update: This object is used to send reply
    :param message: The message to reply with
    :param reply_markup: The keyboard markup to set with the reply
    """
    logging.info("Bot replied to {user_name} with: {message}",
                 user_name=user.username, user_id=user.id, message=message)
    update.message.reply_text(text=message, parse_mode=ParseMode.MARKDOWN,
                              reply_markup=reply_markup)
