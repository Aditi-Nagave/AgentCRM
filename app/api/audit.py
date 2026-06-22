# app/api/audit.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.audit_service import (
    get_audit_history
)

router = APIRouter()


@router.get(
    "/audit/{entity_type}/{entity_id}"
)
def audit(

    entity_type: str,

    entity_id: str,

    db: Session = Depends(get_db)

):

    return get_audit_history(

        db,

        entity_type,

        entity_id
    )