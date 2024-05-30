from pydantic import BaseModel
from datetime import date
from typing import Optional

class Schedule(BaseModel):
    id: str
    child_id: str
    event_name: str
    event_date: date
    notes: Optional[str] = None
