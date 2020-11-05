from datetime import time

from envparse import env

from i18n import Language


class Config:
    def __init__(self):
        self.db_connection_string = env.str("DB_CONNECTION_STRING", default="")
        self.telegram_api_key = env.str("TELEGRAM_API_KEY", default="")
        self.seq_host = env.str("SEQ_LOG_HOST", default="")
        self.start_time = self._read_time(env.str("START_TIME", default="09:00"))
        self.end_time = self._read_time(env.str("END_TIME", default="23:59"))
        self.language = self._read_language(env.str("LANGUAGE", default="tr"))
        self.it_lang_server = env.str("ITALIAN_LANGUAGE_SERVER", default="")

    @staticmethod
    def _read_time(time_str: str) -> time:
        hour = int(time_str.split(":")[0])
        minute = int(time_str.split(":")[1])
        return time(hour, minute)

    @staticmethod
    def _read_language(language_str: str) -> Language:
        if language_str == "tr":
            return Language.TURKISH
        elif language_str == "en":
            return Language.ENGLISH
        elif language_str == "it":
            return Language.ITALIAN


mwexpress_config = Config()
