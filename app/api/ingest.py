# app/api/ingest.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.email_schema import EmailCreate
from app.services.email_ingestion import ingest_email

router = APIRouter()

@router.post("/api/ingest")
def ingest(
    payload: EmailCreate,
    db: Session = Depends(get_db)
):

    return ingest_email(db, payload)