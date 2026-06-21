# app/api/analytics.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.sentiment_trend_service import (
    get_sender_trend
)

router = APIRouter()


@router.get(
    "/analytics/sentiment-trend"
)
def sentiment_trend(

    sender: str,

    db: Session = Depends(get_db)

):

    return get_sender_trend(
        db,
        sender
    )