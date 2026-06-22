# app/api/emails.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.email import Email

router = APIRouter()

@router.get("/emails")
def get_emails(
    db: Session = Depends(get_db)
):
    return db.query(Email)\
        .order_by(
            Email.timestamp.desc()
        )\
        .all()