from datetime import time

from envparse import env

from i18n import Language


class Config:
    def __init__(self):
        self.db_connection_string = env.str("DB_CONNECTION_STRING")
        self.telegram_api_key = env.str("TELEGRAM_API_KEY")
        self.seq_host = env.str("SEQ_LOG_HOST")
        self.start_time = self._read_time(env.str("START_TIME"))
        self.end_time = self._read_time(env.str("END_TIME"))
        self.language = self._read_language(env.str("LANGUAGE"))

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


mwexpress_config = Config()
