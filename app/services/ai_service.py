from sqlalchemy.orm import Session

from app.db.models.ticket import Ticket, TicketStatus
from app.ai.decision import run_ai_decision


CONFIDENCE_THRESHOLD = 0.75


def evaluate_ticket_with_ai(db: Session, ticket: Ticket) -> Ticket:
    decision = run_ai_decision(ticket.subject, ticket.body)

    ticket.priority = decision.priority

    if decision.confidence >= CONFIDENCE_THRESHOLD:
        ticket.status = TicketStatus.resolved
    else:
        ticket.status = TicketStatus.awaiting_review

    db.commit()
    db.refresh(ticket)
    return ticket
