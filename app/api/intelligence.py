# app/api/intelligence.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.reputation_service import (
    scrape_public_sentiment
)

router = APIRouter()


@router.get(
    "/intelligence/reputation"
)
def reputation(

    company: str,

    db: Session = Depends(get_db)

):

    return scrape_public_sentiment(
        db,
        company
    )