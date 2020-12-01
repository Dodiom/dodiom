from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import mwexpress_config
from i18n import Language, Token
from models import User


class Keyboard:
    @staticmethod
    def main(user: User) -> ReplyKeyboardMarkup:
        main_keyboard = [
            [user.language.get(Token.TODAYS_MWE), user.language.get(Token.SUBMIT)],
            [user.language.get(Token.REVIEW), user.language.get(Token.HELP)],
            [user.language.get(Token.SHOW_SCOREBOARD), user.language.get(Token.ACHIEVEMENTS)]
        ]
        return ReplyKeyboardMarkup(main_keyboard)

    @staticmethod
    def remove() -> ReplyKeyboardRemove:
        return ReplyKeyboardRemove()

    @staticmethod
    def submission_category(language: Language) -> ReplyKeyboardMarkup:
        submit_category_keyboard = [
            [language.get(Token.FORMS_SPECIAL_MEANING), language.get(Token.DOES_NOT_FORM_SPECIAL_MEANING)],
            [language.get(Token.CANCEL)],
        ]
        return ReplyKeyboardMarkup(submit_category_keyboard)

    @staticmethod
    def language_selection(language: Language) -> ReplyKeyboardMarkup:
        language_change_keyboard = [
            [language.get(Token.LANGUAGE_ENGLISH)],
            [language.get(Token.LANGUAGE_TURKISH)],
        ]
        return ReplyKeyboardMarkup(language_change_keyboard)

    @staticmethod
    def numeric_keyboard(start: int, end: int):
        return ReplyKeyboardMarkup([[str(x)] for x in range(start, end + 1)])

    @staticmethod
    def review_keyboard(language: Language):
        review_keyboard = [
            [language.get(Token.AGREE_NICE_EXAMPLE)],
            [language.get(Token.DO_NOT_LIKE_EXAMPLE)],
            [language.get(Token.REPORT_SUBMISSION)],
            [language.get(Token.QUIT_REVIEWING)]
        ]
        return ReplyKeyboardMarkup(review_keyboard)

    @staticmethod
    def email_verify_keyboard(language: Language):
        review_keyboard = [
            [language.get(Token.YES), language.get(Token.NO)],
            [language.get(Token.CANCEL)],
        ]
        return ReplyKeyboardMarkup(review_keyboard)
