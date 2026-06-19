# app/schemas/email_schema.pyS
from pydantic import BaseModel
from datetime import datetime

class EmailCreate(BaseModel):

    message_id: str
    sender: str
    subject: str
    body: str
    timestamp: datetime
    thread_id: str