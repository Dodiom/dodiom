from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

from i18n import get_language_token, Language, Token


class Keyboard:
    @staticmethod
    def main(language: Language) -> ReplyKeyboardMarkup:
        main_keyboard = [
            [get_language_token(language, Token.TODAYS_MWE), get_language_token(language, Token.SUBMIT)],
            [get_language_token(language, Token.REVIEW), get_language_token(language, Token.HELP)],
            [get_language_token(language, Token.SHOW_SCOREBOARD), get_language_token(language, Token.CHANGE_LANGUAGE)],
            [get_language_token(language, Token.FEEDBACK)]
        ]
        return ReplyKeyboardMarkup(main_keyboard)

    @staticmethod
    def remove() -> ReplyKeyboardRemove:
        return ReplyKeyboardRemove()

    @staticmethod
    def submission_category(language: Language) -> ReplyKeyboardMarkup:
        submit_category_keyboard = [
            [get_language_token(language, Token.FORMS_SPECIAL_MEANING), get_language_token(language, Token.DOES_NOT_FORM_SPECIAL_MEANING)],
            [get_language_token(language, Token.CANCEL)],
        ]
        return ReplyKeyboardMarkup(submit_category_keyboard)

    @staticmethod
    def language_selection(language: Language) -> ReplyKeyboardMarkup:
        language_change_keyboard = [
            [get_language_token(language, Token.LANGUAGE_ENGLISH)],
            [get_language_token(language, Token.LANGUAGE_TURKISH)],
        ]
        return ReplyKeyboardMarkup(language_change_keyboard)

    @staticmethod
    def numeric_keyboard(start: int, end: int):
        return ReplyKeyboardMarkup([[str(x)] for x in range(start, end + 1)])
