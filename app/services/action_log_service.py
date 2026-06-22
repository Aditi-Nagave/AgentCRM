# app/services/action_log_service.py
import json

from app.models.action import Action


def save_agent_reasoning(
    db,
    email_id,
    action_type,
    reasoning_logs
):

    row = Action(

        email_id=email_id,

        action_type=action_type,

        proposed_content="",

        agent_reasoning_log=json.dumps(
            reasoning_logs
        )
    )

    db.add(row)

    db.commit()

    return row