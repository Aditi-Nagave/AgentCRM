# app/api/respond.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.email import Email

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

    return {
        "email_id": email.id,
        "draft_reply": email.draft_reply,
        "status": "ready_to_send"
    }