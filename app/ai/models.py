# app/ai/models.py
from pydantic import BaseModel
from typing import Dict, List, Optional


class ClassificationResult(BaseModel):

    category: str

    sentiment: str

    sentiment_score: float

    urgency: str

    requires_human: bool

    escalation_reason: Optional[str]

    suggested_reply: Optional[str]

    confidence: float

    is_security: bool

    is_spam: bool

    customer_stage: str

    recommended_action: str

    detected_entities: Dict