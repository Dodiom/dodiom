import enum
import uuid
from enum import auto
from typing import List

from sqlalchemy import Column, Integer, Date, String, ForeignKey, \
    Enum, Boolean, ARRAY, Float, Text, select, func, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, column_property

from i18n import Language

Base = declarative_base()


class MweCategory(enum.Enum):
    VPC = auto()  # verb-particle construction
    VID = auto()  # verbal idiom

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Mwe(Base):
    __tablename__ = 'mwes'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    name = Column(String)
    meaning = Column(String)
    language: Language = Column(Enum(Language))
    lemmas = Column(ARRAY(String))
    category = Column(Enum(MweCategory))
    verb_indices: List[bool] = Column(ARRAY(Boolean))

    submissions = relationship("Submission", back_populates="mwe")
    reviews = relationship("Review", back_populates="mwe")

    def __repr__(self):
        return "<Mwe(name='%s', date='%s', lang='%s')>" % (self.name, self.date, self.language)


class ReviewCategory(enum.Enum):
    LIKE = auto()
    DISLIKE = auto()
    SKIP = auto()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    review_type = Column(Enum(ReviewCategory))
    created = Column(DateTime)

    mwe_id = Column(Integer, ForeignKey('mwes.id'))
    mwe = relationship("Mwe", back_populates="reviews")

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="reviews")

    submission_id = Column(Integer, ForeignKey('submissions.id'))
    submission = relationship("Submission", back_populates="reviews")

    def __repr__(self):
        return "<Review(id='%d', type='%s')>" % (self.id, str(self.review_type))


class SubmissionCategory(enum.Enum):
    POSITIVE_TOGETHER = auto()
    POSITIVE_SEPARATED = auto()
    NEGATIVE_TOGETHER = auto()
    NEGATIVE_SEPARATED = auto()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Submission(Base):
    __tablename__ = 'submissions'

    id = Column(Integer, primary_key=True)
    value = Column(String)
    category = Column(Enum(SubmissionCategory))
    language: Language = Column(Enum(Language))
    lemmas = Column(ARRAY(String))
    words = Column(ARRAY(String))
    points = Column(Float)
    score = Column(Float)
    mwe_words: List[str] = Column(ARRAY(String))
    mwe_indices = Column(ARRAY(Integer))
    conllu = Column(Text)
    hash = Column(String)
    created = Column(DateTime)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="submissions")

    mwe_id = Column(Integer, ForeignKey("mwes.id"))
    mwe = relationship("Mwe", back_populates="submissions")

    reviews: List[Review] = relationship("Review", back_populates="submission")
    review_count = column_property(select([func.count(Review.id)])
                                   .where(Review.submission_id == id))

    def __repr__(self):
        return "<Value(id='%s', value='%s')>" % (self.id, self.value)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    language: Language = Column(Enum(Language))
    viewed_help = Column(Boolean)
    viewed_submission_help = Column(Boolean)
    viewed_review_help = Column(Boolean)
    score = Column(Float)
    score_today_en = Column(Float)
    score_today_tr = Column(Float)
    muted = Column(Boolean)
    created = Column(DateTime)

    submissions: List[Submission] = relationship("Submission", back_populates="user")
    reviews: List[Review] = relationship("Review", back_populates="user")

    def __repr__(self):
        return "<User(id='%s', name='%s')>" % (self.id, self.username)

    def score_today(self) -> float:
        if self.language == Language.ENGLISH:
            return self.score_today_en
        elif self.language == Language.TURKISH:
            return self.score_today_tr
        else:
            return -1


class FeedbackData(Base):
    __tablename__ = 'feedback_data'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

    submission_count = Column(Integer)
    review_count = Column(Integer)
    created = Column(DateTime)

    def __repr__(self):
        return "<Feedback(id='%s')>" % self.id
