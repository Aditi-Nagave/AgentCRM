# app/api/agent_logs.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.agent_log_service import (
    get_agent_logs
)

router = APIRouter()


@router.get(
    "/agent/logs/{email_id}"
)
def agent_logs(
    email_id: int,
    db: Session = Depends(get_db)
):

    return get_agent_logs(
        db,
        email_id
    )