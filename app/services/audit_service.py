# app/services/audit_service.py
from app.models.audit_log import AuditLog


def get_audit_history(

    db,

    entity_type,

    entity_id
):

    return db.query(
        AuditLog
    )\
    .filter(
        AuditLog.entity_type
        == entity_type,

        AuditLog.entity_id
        == str(entity_id)
    )\
    .all()