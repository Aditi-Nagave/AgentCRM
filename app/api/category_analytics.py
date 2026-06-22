# app/api/category_analytics.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.email import Email
from app.core.database import get_db

router = APIRouter()


@router.get(
    "/analytics/category-breakdown"
)
def category_breakdown(
    db: Session = Depends(get_db)
):

    emails = db.query(Email).all()

    output = {}

    for email in emails:

        output[email.category] = (

            output.get(
                email.category,
                0
            ) + 1
        )

    return output