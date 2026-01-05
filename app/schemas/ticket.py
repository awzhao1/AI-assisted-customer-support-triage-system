from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

from app.db.models.ticketstatus import TicketStatus


class TicketCreate(BaseModel):
    subject: str
    body: str
    customer_email: EmailStr


class TicketRead(BaseModel):
    id: UUID
    subject: str
    body: str
    customer_email: EmailStr
    status: TicketStatus
    priority: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True