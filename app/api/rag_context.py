# app/app/rag_context.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.email import Email
from app.rag.retriever import search_policies

router = APIRouter()

@router.get("/workspace/rag/{email_id}")
def get_rag_context(
    email_id:int,
    db:Session=Depends(get_db)
):

    email = db.query(Email)\
        .filter(Email.id == email_id)\
        .first()

    if not email:
        return {
            "error_code":"EMAIL_NOT_FOUND",
            "message":"Email not found",
            "details":{}
        }

    query = f"{email.subject} {email.body}"

    return search_policies(query)