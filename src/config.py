from envparse import env


class Config:
    def __init__(self):
        self.db_connection_string = env.str("DB_CONNECTION_STRING")
        self.telegram_api_key = env.str("TELEGRAM_API_KEY")
        self.seq_host = env.str("SEQ_LOG_HOST")
        self.start_hour = env.int("START_HOUR")
        self.end_hour = env.int("END_HOUR")


mwexpress_config = Config()
