# app/ai/models.py
from pydantic import BaseModel

class ClassificationResult(BaseModel):

    category: str

    sentiment: str

    urgency: str

    requires_human: bool

    confidence: float

    is_security: bool

    is_spam: bool

    customer_stage: str

    recommended_action: str