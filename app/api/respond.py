# app/api/respond.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.action import Action
from app.models.thread import Thread

from app.core.database import get_db
from app.models.email import Email

from app.services.audit_logger import (
    create_audit_log
)


router = APIRouter()

@router.post("/respond/{email_id}")
def respond(
    email_id: int,
    db: Session = Depends(get_db)
):

    email = db.query(Email)\
        .filter(Email.id == email_id)\
        .first()

    if not email:

        return {
            "error_code": "EMAIL_NOT_FOUND",
            "message": "Email not found",
            "details": None
        }
    
    email.status = "Replied"

    action = Action(
        email_id=email.id,
        action_type="Auto-Reply",
        proposed_content=email.draft_reply,
        is_approved=True,
        approved_by="system",
        executed_at=datetime.utcnow()
    )

    db.add(action)

    thread = db.query(Thread)\
       .filter(
           Thread.thread_id ==
           email.thread_id
       )\
       .first()

    if thread:
        thread.status = "Resolved"

    db.commit()

    create_audit_log(
        db,
        "email",
        str(email.id),
        "EMAIL_REPLIED"
    )

    return {
    "status": "sent",
    "email_id": email.id
}