# app/api/threads.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.email import Email

from app.services.thread_workspace_service import (
    get_workspace
)

router = APIRouter()

@router.get("/threads/{email}")
def get_thread(
    email:str,
    db:Session=Depends(get_db)
):
    return get_workspace(
        db,
        email
    )