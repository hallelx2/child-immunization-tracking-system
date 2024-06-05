from pydantic import BaseModel, BeforeValidator, EmailStr, Field
from typing import Annotated, Optional


PyObjectId = Annotated[str, BeforeValidator(str)]
class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False

class UserPublic(BaseModel):
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