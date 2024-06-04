from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from app.core.security import create_access_token, get_password_hash, verify_password
from app.db.repositories.user import UserRepository
from app.db.models.user import User, UserCreate, UserInDB, UserPublic
from app.db.base import database

router = APIRouter()

UserDep= Annotated[UserRepository, Depends()]

@router.post("/register")
async def register_user(user_create: UserCreate, user_repo: UserDep):

    user = await user_repo.get_user_by_email(user_create.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user_create.password)

    user_in_db = UserInDB(**user_create.model_dump(), hashed_password=hashed_password)
    user = User(**user_in_db.model_dump())

    await user_repo.create_user(user)

    return {"msg": "User registered successfully"}

@router.post("/login")
async def login_user(user_login: UserCreate, user_repo: Annotated[UserRepository, Depends()]):
    
    user = await user_repo.get_user_by_email(user_login.email)
    if not user:
        raise HTTPException(status_code=400, detail="User doesn't exist")
    
    if not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect login credentials")
    
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Inactive user")

    access_token = create_access_token(user.email)

    return UserPublic(access_token=access_token, **user)


#TODO: create an endpoint for googles oauth2 callback