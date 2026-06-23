# app/api/agent.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.email import Email

from app.agent.planner import build_plan

router = APIRouter()


@router.post("/agent/dry-run/{email_id}")
def dry_run(
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

    classification = {

        "category":email.category,

        "urgency":email.urgency
    }

    plan = build_plan(
        classification
    )

    trace = []

    for step in plan:

        trace.append({

            "thought":
            f"Need {step}",

            "action":
            step,

            "observation":
            "Would execute tool",

            "next_step":
            "Continue"

        })

    return {

        "executed":False,

        "trace":trace
    }