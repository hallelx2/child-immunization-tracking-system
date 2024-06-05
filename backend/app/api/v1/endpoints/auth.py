from fastapi import APIRouter, HTTPException
from app.core.security import create_access_token, get_password_hash, verify_password
from app.db.models.user import User, UserCreate, UserInDB, UserLogin, UserPublic
from app.db.base import user_repo

router = APIRouter()

@router.post("/register")
async def register_user(user_create: UserCreate):

    user = await user_repo.get_user_by_email(user_create.email)
    print(user)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user_create.password)

    user_in_db = UserInDB(**user_create.model_dump(), hashed_password=hashed_password)
    user = User(**user_in_db.model_dump())

    await user_repo.create_user(user)

    return {"msg": "User registered successfully"}

@router.post("/login")
async def login_user(user_login: UserLogin):
    
    user = await user_repo.get_user_by_email(user_login.email)
    user = User(**user)

    if not user:
        raise HTTPException(status_code=400, detail="User doesn't exist")
    
    if not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect login credentials")
    
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Inactive user")

    access_token = create_access_token(user.email)

    return UserPublic(access_token=access_token, **user.model_dump())


#TODO: create an endpoint for googles oauth2 callback