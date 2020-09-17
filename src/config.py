from datetime import time

from envparse import env


class Config:
    def __init__(self):
        self.db_connection_string = env.str("DB_CONNECTION_STRING")
        self.telegram_api_key = env.str("TELEGRAM_API_KEY")
        self.seq_host = env.str("SEQ_LOG_HOST")
        self.start_time = self._read_time(env.str("START_TIME"))
        self.end_time = self._read_time(env.str("END_TIME"))

    @staticmethod
    def _read_time(time_str: str) -> time:
        hour = int(time_str.split(":")[0])
        minute = int(time_str.split(":")[1])
        return time(hour, minute)


mwexpress_config = Config()
