# app/services/thread_workspace_service.py
from app.models.email import Email
from app.models.contact import Contact
from app.models.action import Action

from app.services.agent_log_service import (
    get_agent_logs
)

def get_workspace(
    db,
    email
):

    emails = db.query(
        Email
    ).filter(
        Email.sender == email
    ).order_by(
        Email.timestamp
    ).all()

    contact = db.query(
        Contact
    ).filter(
        Contact.email == email
    ).first()

    actions = []

    if emails:

        email_ids = [
            e.id
            for e in emails
        ]

        actions = db.query(
            Action
        ).filter(
            Action.email_id.in_(
                email_ids
            )
        ).all()

    agent_logs = []

    for e in emails:

        logs = get_agent_logs(
            db,
            e.id
        )

        agent_logs.extend(
            logs
        )

    return {
        "contact": contact,
        "emails": emails,
        "actions": actions,
        "agent_logs": agent_logs
    }