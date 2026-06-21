# app/services/email_ingestion.py
import json
from app.models.email import Email
from app.services.deduplication import is_duplicate
from app.services.thread_service import create_thread_if_not_exists
from app.services.intelligence_engine import process_email

from app.services.validation_service import (
    validate_email_payload,
    truncate_body
)

from app.services.priority_service import (
    calculate_priority
)

from app.services.internal_detector import (
    is_internal_email
)

from app.services.internal_detector import (
is_internal_email
)

from app.services.spam_detector import (
detect_spam
)

from app.services.security_detector import (
detect_security
)

from app.services.urgency_detector import (
detect_urgency
)


def ingest_email(db, payload):

    validate_email_payload(
        payload.subject,
        payload.body
    )

    body = truncate_body(payload.body)

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

    text = payload.subject + " " + body

    is_spam = detect_spam( payload.subject, body )
    is_security = detect_security( text )
    urgency = detect_urgency( text )
    internal = is_internal_email( payload.sender )
    priority_score = calculate_priority( urgency, is_security, is_spam )

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

    body=body,

    timestamp=payload.timestamp,

    thread_id=payload.thread_id,

    category=analysis["category"],

    urgency=urgency,

    priority_score=priority_score,

    sentiment=analysis["sentiment"],

    requires_human=analysis["requires_human"],

    confidence=analysis["confidence"],

    is_spam=is_spam,

    is_security=is_security,

    is_internal=internal,

    customer_stage=analysis["customer_stage"],

    recommended_action=analysis["recommended_action"],

    draft_reply=analysis["draft_reply"],

    agent_log=json.dumps(analysis["agent_logs"]),

    knowledge_used=True
)

    db.add(email)
    db.commit()

    return {
        "status": "success",
        "message": "Email Stored"
    }