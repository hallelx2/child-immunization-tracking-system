from pydantic import BaseModel
from typing import Optional
from datetime import date

class ChildProfile(BaseModel):
    id: str
    user_id: str
    first_name: str
    last_name: str
    date_of_birth: date
    gender: Optional[str] = None
    notes: Optional[str] = None
