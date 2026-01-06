import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from .ticketstatus import TicketStatus, TicketIntent
from app.db.base import Base



# Database declaration
class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    customer_email = Column(String(255), nullable=False)

    status = Column(
        Enum(TicketStatus),
        nullable=False,
        default=TicketStatus.new,
    )

    priority = Column(String(50), nullable=True)
    intent = Column(
        Enum(TicketIntent),
        nullable = False,
        default = TicketIntent.unknown,
    )
    suggestion = Column(Text, nullable=False, default="")
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )
