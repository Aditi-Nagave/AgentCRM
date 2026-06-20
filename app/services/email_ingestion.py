# app/services/email_ingestion.py
from app.models.email import Email
from app.services.deduplication import is_duplicate
from app.services.thread_service import create_thread_if_not_exists
from app.services.intelligence_engine import process_email

def ingest_email(db, payload):

    if is_duplicate(db, payload.message_id):

        return {
            "status": "error",
            "message": "Duplicate Email"
        }

    create_thread_if_not_exists(
        db,
        payload.thread_id,
        payload.subject,
        payload.sender
    )

    analysis = process_email(
             db,
             payload.thread_id,
             payload.subject,
             payload.body
    )

    email = Email(

    message_id=payload.message_id,

    sender=payload.sender,

    subject=payload.subject,

    body=payload.body,

    timestamp=payload.timestamp,

    thread_id=payload.thread_id,

    category=analysis["category"],

    urgency=analysis["urgency"],

    sentiment=analysis["sentiment"],

    requires_human=analysis["requires_human"],

    confidence=analysis["confidence"],

    is_spam=analysis["is_spam"],

    is_security=analysis["is_security"],

    customer_stage=analysis["customer_stage"],

    recommended_action=analysis["recommended_action"],

    draft_reply=analysis["draft_reply"],

    knowledge_used=True
)

    db.add(email)
    db.commit()

    return {
        "status": "success",
        "message": "Email Stored"
    }