from sqlalchemy import Column, Integer, DateTime, String, Date, Boolean, Text, ForeignKey, UniqueConstraint
from sqlalchemy import func
from database import Base

#User Table
class User(Base):
    __tablename__ = "users"

    #fields
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, nullable=False)
    hashed_password = Column(String(20), nullable=False)

#Categories Table
class Category(Base):
    __tablename__ = "categories"

    #fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

#Habits Table
class Habit(Base):
    __tablename__ = "habits"

    #fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    current_streak = Column(Integer, nullable=False, default=0)
    longest_streak = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

#Check-Ins Table
class Check_In(Base):
    __tablename__ = "check_ins"

    #fiels
    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    the_date = Column(Date, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
    notes = Column(Text)
    __table_args__ = (UniqueConstraint("habit_id", "the_date"),)