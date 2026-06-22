# app/services/contact_service.py
from app.models.contact import Contact
from app.services.audit_logger import (
    create_audit_log
)

def get_contact(
    db,
    email
):

    return db.query(Contact)\
        .filter(
            Contact.email == email
        )\
        .first()


def update_status(
    db,
    email,
    status
):

    contact = get_contact(
        db,
        email
    )

    if not contact:
        return None
    
    old_status = contact.status
    contact.status = status

    db.commit()

    create_audit_log(
        db,
        "Contact",
        contact.id,
        "CONTACT_STATUS_UPDATED",
        diff={"old_status": old_status, "new_status": status}
    )

    return contact