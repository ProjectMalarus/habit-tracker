from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

#--------USER SCHEMAS--------
class UserCreate(BaseModel):
    username: str
    password: str #plain text will be hashed in CRUD

class UserResponse(BaseModel):
    id: int
    username: str 

    class Config:
        from_attributes = True

#--------HABIT SCHEMAS--------
class HabitCreate(BaseModel):
    name: str
    category_id: Optional[int] = None #Optional field
    user_id: int

class HabitResponse(BaseModel):
    id: int
    name: str
    user_id: int
    category_id: Optional[int] = None
    current_streak: int
    longest_streak: int
    created_at: datetime

    class Config:
        from_attributes = True

#--------CATEGORY SCHEMAS--------
class CategoryCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True

class CategoryResponse(BaseModel):
    id: int
    name: str

#--------CHECK-IN SCHEMAS--------
class CheckInCreate(BaseModel):
    habit_id: int
    the_date: date
    completed: bool
    notes: Optional[str] = None

    class Config:
        from_attributes = True

class CheckInResponse(BaseModel):
    id: int
    habit_id: int
    the_date: date
    completed: bool
    notes: Optional[str] = None

    class Config:
            from_attributes = True