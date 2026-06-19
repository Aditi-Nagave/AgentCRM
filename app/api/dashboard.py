# app/api/dashboard.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.email import Email
from app.core.database import get_db

router = APIRouter()

@router.get("/dashboard/stats")

def dashboard_stats(
        db: Session = Depends(get_db)
):

    return {

        "total_emails":
        db.query(Email).count(),

        "spam":
        db.query(Email)
        .filter(Email.is_spam == True)
        .count(),

        "critical":
        db.query(Email)
        .filter(Email.urgency == "Critical")
        .count(),

        "security":
        db.query(Email)
        .filter(Email.is_security == True)
        .count()
    }