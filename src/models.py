import enum
from enum import auto

from sqlalchemy import Column, Integer, Date, String, ForeignKey, Enum, Boolean, ARRAY, Float
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from database import Base
from i18n import Language


class Mwe(Base):
    __tablename__ = 'mwes'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    name = Column(String)
    meaning = Column(String)
    language = Column(Enum(Language))
    lemmas = Column(ARRAY(String))

    submissions = relationship("Submission", back_populates="mwe")
    reviews = relationship("Review", back_populates="mwe")

    def __repr__(self):
        return "<Mwe(name='%s', date='%s', lang='%s')>" % (self.name, self.date, self.language)


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    review_type = Column(Integer)

    mwe_id = Column(Integer, ForeignKey('mwes.id'))
    mwe = relationship("Mwe", back_populates="reviews")

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="reviews")

    submission_id = Column(Integer, ForeignKey('submissions.id'))
    submission = relationship("Submission", back_populates="reviews")

    def __repr__(self):
        return "<Review(id='%s', type='%d')>" % (self.id, self.review_type)


class SubmissionCategory(enum.Enum):
    POSITIVE_TOGETHER = auto()
    POSITIVE_SEPARATED = auto()
    NEGATIVE_TOGETHER = auto()
    NEGATIVE_SEPARATED = auto()


class Submission(Base):
    __tablename__ = 'submissions'

    id = Column(Integer, primary_key=True)
    value = Column(String)
    category = Column(Enum(SubmissionCategory))
    language = Column(Enum(Language))
    lemmas = Column(ARRAY(String))
    words = Column(ARRAY(String))
    points = Column(Float)
    mwe_words = Column(ARRAY(String))

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="submissions")

    mwe_id = Column(Integer, ForeignKey("mwes.id"))
    mwe = relationship("Mwe", back_populates="submissions")

    reviews = relationship("Review", back_populates="submission")

    @hybrid_property
    def review_count(self):
        return len(self.reviews)

    def __repr__(self):
        return "<Value(id='%s', value='%s')>" % (self.id, self.value)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    language = Column(Enum(Language))
    viewed_help = Column(Boolean)

    submissions = relationship("Submission", back_populates="user")
    reviews = relationship("Review", back_populates="user")

    def __repr__(self):
        return "<User(id='%s', name='%s')>" % (self.id, self.username)
