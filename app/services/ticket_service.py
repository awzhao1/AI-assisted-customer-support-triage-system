from sqlalchemy.orm import Session
from uuid import UUID

from app.db.models.ticket import Ticket, TicketStatus
from app.schemas.ticket import TicketCreate


def create_ticket(db: Session, data: TicketCreate) -> Ticket:
    ticket = Ticket(
        subject=data.subject,
        body=data.body,
        customer_email=data.customer_email,
        status=TicketStatus.new,
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_ticket(db: Session, ticket_id: UUID) -> Ticket | None:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def list_tickets(db: Session) -> list[Ticket]:
    return db.query(Ticket).order_by(Ticket.created_at.desc()).all()
