# app/services/deduplication.py
from app.models.email import Email

def is_duplicate(db, message_id):

    existing = db.query(Email).filter(
        Email.message_id == message_id
    ).first()

    return existing is not None