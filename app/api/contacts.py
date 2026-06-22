# app/api/contacts.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.contact_service import (
    get_contact,
    update_status
)

router = APIRouter()


@router.get(
    "/contacts/{email}"
)
def contact(

    email: str,

    db: Session = Depends(get_db)

):

    return get_contact(
        db,
        email
    )


@router.patch(
    "/contacts/{email}/status"
)
def update_contact_status(

    email: str,

    payload: dict,

    db: Session = Depends(get_db)

):

    status = payload.get("status")

    if not status:
        return {
            "error": "status field required"
        }

    update_status(
         db,
         email,
         status
       )

    return {
        "status": "updated"
    }