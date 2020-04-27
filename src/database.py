import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_host = os.environ["DB_HOST"]
db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]
engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# noinspection PyUnresolvedReferences
def init_database() -> None:
    from models import User, Mwe, Submission, Review

    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    logging.info("Database initialized.")
