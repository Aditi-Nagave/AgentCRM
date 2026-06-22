# app/services/draft_service.py
from app.models.email import Email


def update_draft(
    db,
    email_id,
    draft
):

    email = db.query(Email)\
        .filter(Email.id == email_id)\
        .first()

    if not email:
        return None

    email.draft_reply = draft

    db.commit()

    return email


def approve_draft(
    db,
    email_id
):

    email = db.query(Email)\
        .filter(Email.id == email_id)\
        .first()

    if not email:
        return None

    email.recommended_action = "Reply Sent"

    db.commit()

    return email