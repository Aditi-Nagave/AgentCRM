# app/services/contact_service.py
from app.models.contact import Contact


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

    contact.status = status

    db.commit()

    return contact