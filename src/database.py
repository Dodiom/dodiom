import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session

from config import mwexpress_config
from log import mwelog


class Database:
    def __init__(self):
        self.engine = create_engine(mwexpress_config.db_connection_string, echo=False)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        self.session = self.Session()
        self.commit_lock = threading.Lock()

        # noinspection PyUnresolvedReferences
        from models import User, Mwe, Submission, Review, FeedbackData, Achievement, Base
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(self.engine)
        mwelog.info("Database initialized.")

    def get_session(self) -> Session:
        return self.session

    def commit(self, session: Session):
        with self.commit_lock:
            try:
                session.commit()
                session.flush()
            except:
                session.rollback()
                raise

    def reset_database(self) -> None:
        # noinspection PyUnresolvedReferences
        from models import User, Mwe, Submission, Review, FeedbackData, Achievement, Base
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)


database = Database()
