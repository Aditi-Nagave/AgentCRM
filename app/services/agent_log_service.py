# app/services/agent_log_service.py
import json

from app.models.action import Action


def get_agent_logs(
    db,
    email_id
):

    rows = db.query(Action)\
        .filter(
            Action.email_id == email_id
        )\
        .all()

    output = []

    for row in rows:

        try:

            reasoning = json.loads(
                row.agent_reasoning_log
            )

        except:

            reasoning = []

        output.append({

            "action_id": row.id,

            "email_id": row.email_id,

            "action_type": row.action_type,

            "is_approved": row.is_approved,

            "approved_by": row.approved_by,

            "executed_at": (
                str(row.executed_at)
                if row.executed_at
                else None
            ),

            "reasoning_trace":
            reasoning
        })

    return output