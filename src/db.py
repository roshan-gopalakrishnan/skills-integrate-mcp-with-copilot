from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./dev.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Association table for students signing up for activities
class Signup(Base):
    __tablename__ = 'signups'
    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    schedule = Column(String, nullable=True)
    max_participants = Column(Integer, nullable=True)
    participants = relationship("Student", secondary="signups", back_populates="activities")


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=True)
    activities = relationship("Activity", secondary="signups", back_populates="participants")


def init_db():
    Base.metadata.create_all(bind=engine)


def seed_db(session):
    """Populate initial activities if the table is empty."""
    if session.query(Activity).count() == 0:
        initial = [
            {
                "name": "Chess Club",
                "description": "Learn strategies and compete in chess tournaments",
                "schedule": "Fridays, 3:30 PM - 5:00 PM",
                "max_participants": 12,
            },
            {
                "name": "Programming Class",
                "description": "Learn programming fundamentals and build software projects",
                "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
                "max_participants": 20,
            },
            {
                "name": "Gym Class",
                "description": "Physical education and sports activities",
                "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
                "max_participants": 30,
            },
        ]

        for a in initial:
            activity = Activity(**a)
            session.add(activity)
        session.commit()
