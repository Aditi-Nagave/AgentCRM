# app/api/intelligence.py
from fastapi import APIRouter

from app.services.reputation_service import (
    scrape_public_sentiment
)

router = APIRouter()


@router.get(
    "/intelligence/reputation"
)
def reputation(

    company: str = "Company"

):

    return scrape_public_sentiment(
        company
    )