# app/api/respond.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

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
    
    create_audit_log(

        db,

        "email",

        email_id,

        "EMAIL_SENT"
    )

    return {
        "email_id": email.id,
        "draft_reply": email.draft_reply,
        "status": "ready_to_send"
    }