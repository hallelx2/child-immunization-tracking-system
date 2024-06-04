from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False

class UserPublic(BaseModel):
    id: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False
    access_token: str | None = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class UserInDB(UserCreate):
    hashed_password: str