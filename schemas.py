from pydantic import BaseModel
from datetime import datetime, date

#User schemas
class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    pass

class HabitCreate(BaseModel):
    name: str
    createdAt: datetime
