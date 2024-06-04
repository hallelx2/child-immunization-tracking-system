from datetime import timedelta, timezone, datetime
from typing import Optional, Union
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(subject: Union[str, int], 
                        expires_delta: Optional[timedelta] = None) -> str:
    '''Create an access JSON Web Tokens.

    Args:
        subject (Union[str, Any]): subject for the token, could be user email.
        expires_delta (timedelta): the time interval of the token validity.

    Returns:
        str: created JWT.

    '''
    if not expires_delta:
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {"exp": expire.timestamp(), "sub": str(subject)}

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY,
                             algorithm=settings.JWT_ENCODE_ALGORITHM)
    
    return encoded_jwt
