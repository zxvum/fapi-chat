from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MessageRead(BaseModel):
    id: int
    client_id: int
    message: str
    created_at: Optional[datetime]


class MessageCreate(BaseModel):
    client_id: int
    message: str
