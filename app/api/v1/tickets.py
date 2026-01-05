from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from .deps import get_db
from app.services.ai_service import evaluate_ticket_with_ai
from app.schemas.ticket import TicketCreate, TicketRead
from app.db.models.ticketstatus import TicketStatus
from app.services.ticket_service import (
    create_ticket,
    get_ticket,
    list_tickets,
)

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("/", response_model=TicketRead)
def create_ticket_endpoint(
    payload: TicketCreate,
    db: Session = Depends(get_db),
):
    return create_ticket(db, payload)


@router.get("/{ticket_id}", response_model=TicketRead)
def get_ticket_endpoint(
    ticket_id: UUID,
    db: Session = Depends(get_db),
):
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.get("/", response_model=list[TicketRead])
def list_tickets_endpoint(
    db: Session = Depends(get_db),
):
    return list_tickets(db)


@router.post("/{ticket_id}/ai-evaluate", response_model=TicketRead)
def ai_evaluate_ticket(
    ticket_id: UUID,
    db: Session = Depends(get_db),
):
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    if ticket.status != TicketStatus.new:
        raise HTTPException(
            status_code=400,
            detail="Ticket already processed",
        )

    return evaluate_ticket_with_ai(db, ticket)