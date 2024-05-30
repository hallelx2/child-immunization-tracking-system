from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: str
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False
