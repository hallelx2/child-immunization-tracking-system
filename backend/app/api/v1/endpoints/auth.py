from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from app.core.security import get_password_hash, verify_password
from app.db.repositories.user import UserRepository
from app.db.models.user import User

router = APIRouter()

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class UserInDB(UserCreate):
    hashed_password: str

@router.post("/register")
async def register_user(user_create: UserCreate, user_repo: UserRepository = Depends()):
    user = await user_repo.get_user_by_email(user_create.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_create.password)
    user_in_db = UserInDB(**user_create.dict(), hashed_password=hashed_password)
    await user_repo.create_user(user_in_db)
    return {"msg": "User registered successfully"}
