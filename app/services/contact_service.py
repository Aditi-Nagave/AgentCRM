# app/services/contact_service.py
from app.models.contact import Contact
from app.services.audit_logger import (
    create_audit_log
)


def create_contact_if_not_exists(
    db,
    email
):

    contact = db.query(Contact)\
        .filter(
            Contact.email == email
        )\
        .first()

    if contact:
        return contact

    contact = Contact(

        email=email,

        name=email.split("@")[0],

        company=email.split("@")[-1],

        status="Active",

        account_value=0,

        churn_risk_score=0
    )

    db.add(contact)

    db.commit()

    db.refresh(contact)

    return contact

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