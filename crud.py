from hash_password import create_hashed_password
from sqlalchemy.orm import Session
import exceptions
import schemas
import models

#--------USER CRUD--------
def create_user(db : Session, user: schemas.UserCreate):
    hashed_pw = create_hashed_password(user.password)
    db_user = models.User(username = user.username, hashed_password = hashed_pw)
    if db.query(models.User).filter(models.User.username == db_user.username).first():
        raise exceptions.UserAlreadyExistsError(f"This username is already taken")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, user_username: str):
    return db.query(models.User).filter(models.User.username == user_username).first()

#--------HABIT CRUD--------
def create_habit(db: Session, habit: schemas.HabitCreate):
    db_habit = models.Habit(**habit.model_dump())
    db.add(db_habit)    
    db.commit()
    db.refresh(db_habit)

def get_habits_by_user(db: Session, user: models.User):
    return db.query(models.Habit).filter(models.Habit.user_id == user.id).all()

def delete_habit(db: Session, habit: models.Habit):
    db.delete(habit)
    db.commit()

#--------CATEGORY CRUD--------
def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()

#--------CHECK-IN CRUD--------
def create_check_in(db: Session, check_in: schemas.CheckInCreate):
    db_check_in = models.Check_In(**check_in.model_dump())
    db.add(db_check_in)
    db.commit()
