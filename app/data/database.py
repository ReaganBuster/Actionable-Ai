from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class UserReview(Base):
    __tablename__ = 'user_reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String, nullable=False)
    review = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    date = Column(Date, default=datetime.date.today)

class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    report = Column(Text, nullable=False)

class CurrentReport(Base):
    __tablename__ = 'current_report'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    report = Column(Text, nullable=False)

# Create an SQLite database
engine = create_engine('sqlite:///actionable_ai.db')
Base.metadata.create_all(engine)



