# app/ai/schemas.py
from pydantic import BaseModel, Field
from typing import Literal


class AIDecision(BaseModel):
    intent: Literal[
        "billing",
        "technical_issue",
        "account",
        "general_question",
        "unknown",
    ]
    priority: Literal["low", "medium", "high"]
    confidence: float = Field(ge=0.0, le=1.0)
