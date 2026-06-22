# app/services/audit_logger.py
import json

from app.models.audit_log import AuditLog


def create_audit_log(
    db,
    entity_type,
    entity_id,
    action,
    performed_by="system",
    diff=None
):

    row = AuditLog(

        entity_type=entity_type,

        entity_id=str(entity_id),

        action=action,

        performed_by=performed_by,

        diff=json.dumps(diff or {})
    )

    db.add(row)

    db.commit()

    return row