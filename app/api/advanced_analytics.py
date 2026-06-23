# app/api/advanced_analytics.py
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.email import Email
from app.core.database import get_db

router = APIRouter()


@router.get("/analytics/risk-accounts")
def risk_accounts(
    db:Session=Depends(get_db)
):

    emails = db.query(Email).all()

    output = []

    for e in emails:

        if e.sentiment_score < 0:

            output.append({

                "sender":e.sender,
                "subject":e.subject,
                "score":e.sentiment_score

            })

    return output


@router.get("/analytics/agent-metrics")
def agent_metrics(
    db:Session=Depends(get_db)
):

    emails = db.query(Email).all()

    return {

        "total_processed":len(emails),

        "human_required":
        len(
            [e for e in emails
            if e.requires_human]
        ),

        "auto_replied":
        len(
            [e for e in emails
            if e.recommended_action ==
            "Reply Sent"]
        ),

        "security":
        len(
            [e for e in emails
            if e.is_security]
        )
    }


@router.get("/analytics/response-heatmap")
def response_heatmap(
    db:Session=Depends(get_db)
):

    emails = db.query(Email).all()

    buckets = {}

    for e in emails:

        hour = e.timestamp.hour

        buckets[hour] = buckets.get(hour,0)+1

    return buckets