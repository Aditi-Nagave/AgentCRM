# app/api/threads.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.email import Email

router = APIRouter()

@router.get("/threads/{email}")

def get_thread(
        email: str,
        db: Session = Depends(get_db)
):

    data = db.query(Email)\
        .filter(Email.sender == email)\
        .order_by(Email.timestamp)\
        .all()

    return data