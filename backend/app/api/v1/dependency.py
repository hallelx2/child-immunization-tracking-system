from jose import JWTError, jwt
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, OAuth2PasswordBearer
from pydantic import ValidationError

from app.db.base import database
from app.core.config import settings
from app.db.models.user import UserPublic
from app.db.repositories.user import UserRepository

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)
http_auth = HTTPBearer()


TokenDep = Annotated[str, Depends(oauth2_scheme)]
UserDep= Annotated[UserRepository, Depends()]

async def get_current_user(token: TokenDep, user_repo: UserDep) -> UserPublic:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.JWT_ENCODE_ALGORITHM]
        )
        token_data = payload.get("sub")

        if not token:
            raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            )

    except (ValidationError, JWTError):
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
        )
    
    user = await user_repo.get_user_by_email(token_data) # type: ignore
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return UserPublic(**user)

CurrentUser = Annotated[UserPublic, Depends(get_current_user)]


async def get_current_superuser(current_user: CurrentUser) -> UserPublic:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="The user doesn't have enough privileges"
        )
    return current_user

SuperUser = Annotated[UserPublic, Depends(get_current_superuser)]