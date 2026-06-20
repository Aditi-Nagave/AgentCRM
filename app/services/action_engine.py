# app/services/action_engine.py
from app.ai.action_generator import (
    generate_action
)

from app.ai.reply_generator import (
    generate_reply
)


def process_action_engine(
        subject,
        body,
        classification,
        knowledge
):

    action = generate_action(
        classification,
        knowledge
    )

    draft_reply = generate_reply(
        subject,
        body,
        classification,
        action,
        knowledge
    )

    return {

        "recommended_action":
        action,

        "draft_reply":
        draft_reply
    }