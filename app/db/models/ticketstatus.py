from enum import Enum

class TicketStatus(str, Enum):
    new = "new"
    processing = "processing"
    awaiting_review = "awaiting_review"
    resolved = "resolved"
    failed = "failed"