import datetime
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
    date = Column(Date, nullable=False)
    name = Column(String, nullable=False)
    meaning = Column(String, nullable=False)
    language: Language = Column(Enum(Language), nullable=False)
    lemmas: List[str] = Column(ARRAY(String))
    category: MweCategory = Column(Enum(MweCategory), nullable=False)

    submissions: List['Submission'] = relationship("Submission", back_populates="mwe")
    reviews: List['Review'] = relationship("Review", back_populates="mwe")

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
    review_type: ReviewCategory = Column(Enum(ReviewCategory))
    created = Column(DateTime, default=datetime.datetime.now, nullable=False)

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
    value = Column(String, nullable=False)
    category: SubmissionCategory = Column(Enum(SubmissionCategory))
    language: Language = Column(Enum(Language))
    lemmas: List[str] = Column(ARRAY(String))
    words: List[str] = Column(ARRAY(String))
    points = Column(Float, default=0, nullable=False)
    score = Column(Float, default=0, nullable=False)
    mwe_words: List[str] = Column(ARRAY(String))
    mwe_indices: List[int] = Column(ARRAY(Integer))
    conllu = Column(Text)
    hash = Column(String, default="", nullable=False)
    created = Column(DateTime, default=datetime.datetime.now, nullable=False)
    flagged = Column(Boolean, default=False, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="submissions")

    mwe_id = Column(Integer, ForeignKey("mwes.id"))
    mwe = relationship("Mwe", back_populates="submissions")

    reviews: List[Review] = relationship("Review", back_populates="submission")
    review_count: int = column_property(select([func.count(Review.id)])
                                        .where(Review.submission_id == id))

    def __repr__(self):
        return "<Value(id='%s', value='%s')>" % (self.id, self.value)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    language: Language = Column(Enum(Language))
    viewed_help = Column(Boolean, default=False, nullable=False)
    viewed_todays_mwe_help = Column(Boolean, default=False, nullable=False)
    viewed_submission_help = Column(Boolean, default=False, nullable=False)
    viewed_review_help = Column(Boolean, default=False, nullable=False)
    score = Column(Float, default=0.0, nullable=False)
    score_today_en = Column(Float, default=0.0, nullable=False)
    score_today_tr = Column(Float, default=0.0, nullable=False)
    muted = Column(Boolean, default=False, nullable=False)
    created = Column(DateTime, default=datetime.datetime.now, nullable=False)

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

    submission_count = Column(Integer, nullable=False)
    review_count = Column(Integer, nullable=False)
    created = Column(DateTime, default=datetime.datetime.now, nullable=False)

    def __repr__(self):
        return "<Feedback(id='%s')>" % self.id


class AchievementType(enum.Enum):
    FIRST_SUBMISSION = auto()  # submit first submission
    EARLY_BIRD = auto()  # submit in the first half hour
    SUB_LVL_1 = auto()  # submit 5 examples
    SUB_LVL_2 = auto()  # review 10 examples
    SUB_LVL_3 = auto()  # review 20 examples
    SUB_LVL_4 = auto()  # review 40 examples
    SUB_LVL_5 = auto()  # review 70 examples
    REVIEW_LVL_1 = auto()  # submit 10 examples
    REVIEW_LVL_2 = auto()  # review 20 examples
    REVIEW_LVL_3 = auto()  # review 40 examples
    REVIEW_LVL_4 = auto()  # review 80 examples
    REVIEW_LVL_5 = auto()  # review 160 examples


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Achievement(Base):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

    type = Column(Enum(AchievementType), nullable=False)
    created = Column(DateTime, default=datetime.datetime.now, nullable=False)

    def __repr__(self):
        return "<Attachment(user='%s', type='%s')>" % (self.user.username, self.type)
