import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import mwexpress_config


class Database:
    def __init__(self):
        self.engine = create_engine(mwexpress_config.db_connection_string, echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # noinspection PyUnresolvedReferences
        from models import User, Mwe, Submission, Review, FeedbackData, Base
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(self.engine)
        logging.info("Database initialized.")

    def get_session(self) -> Session:
        return self.session

    def reset_database(self) -> None:
        # noinspection PyUnresolvedReferences
        from models import User, Mwe, Submission, Review, FeedbackData, Base
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)


database = Database()
session = database.get_session()
