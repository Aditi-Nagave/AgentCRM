# app/api/drafts.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.draft_service import (
    update_draft,
    approve_draft
)

router = APIRouter()


@router.patch("/drafts/{id}")
def edit_draft(

    id: int,

    payload: dict,

    db: Session = Depends(get_db)

):

    email = update_draft(
        db,
        id,
        payload["draft"]
    )

    return {
        "status": "updated",
        "email_id": id
    }


@router.post(
    "/drafts/{id}/approve"
)
def approve(
    id: int,
    db: Session = Depends(get_db)
):

    approve_draft(
        db,
        id
    )

    return {
        "status": "approved"
    }