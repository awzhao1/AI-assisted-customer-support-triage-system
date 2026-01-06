from enum import Enum

class TicketStatus(str, Enum):
    new = "new"
    processing = "processing"
    awaiting_review = "awaiting_review"
    resolved = "resolved"
    failed = "failed"

class TicketIntent(str, Enum):
    billing = "billing",
    technical_issue = "technical_issue",
    account = "account",
    general_question = "general_question",
    unknown = "unknown",