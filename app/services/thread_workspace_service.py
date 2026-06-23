# app/services/thread_workspace_service.py
from app.models.email import Email
from app.models.action import Action
from app.models.audit_log import AuditLog

def get_workspace(
    db,
    sender
):

    emails = db.query(Email)\
        .filter(
            Email.sender==sender
        )\
        .all()

    actions = db.query(Action).all()

    audit = db.query(AuditLog).all()

    return {

        "emails":emails,

        "actions":actions,

        "audit":audit
    }