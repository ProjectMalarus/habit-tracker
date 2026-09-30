from models import User
from hash_password import create_hashed_password
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas

def create_User(db : Session, username: str, password : str):
    myUser = User()
    myUser.username = username
    myUser.hashed_password = create_hashed_password(password)
    db.add(myUser)
    db.commit()

mySession = SessionLocal()

create_User(mySession, "malachi", "password")

mySession.close()