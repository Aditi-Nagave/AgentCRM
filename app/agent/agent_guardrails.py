# app/agent/agent_guardrails.py
def enforce_agent_guardrails(
    classification,
    plan
):

    urgency = classification.get(
        "urgency",
        "Low"
    )

    if urgency == "Critical":

        filtered = []

        for step in plan:

            if step != "send_auto_reply":

                filtered.append(step)

        if "escalate_to_human" not in filtered:

            filtered.append(
                "escalate_to_human"
            )

        return filtered

    return plan