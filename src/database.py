import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class Database:
    def __init__(self):
        db_host = os.environ["DB_HOST"]
        db_user = os.environ["DB_USER"]
        db_pass = os.environ["DB_PASSWORD"]
        db_name = os.environ["DB_NAME"]
        self.engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}', echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # noinspection PyUnresolvedReferences
        from models import User, Mwe, Submission, Review, Base
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(self.engine)
        logging.info("Database initialized.")

    def get_session(self) -> Session:
        return self.session

    def reset_database(self) -> None:
        from models import User, Mwe, Submission, Review, Base
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)


database = Database()
session = database.get_session()
