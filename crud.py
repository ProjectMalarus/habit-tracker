from dependencies import get_db
from models import User
from hash_password import create_hashed_password
from sqlalchemy.orm import Session

myUser = User()
myUser.hashed_password = create_hashed_password("password")

def addUser(db = )