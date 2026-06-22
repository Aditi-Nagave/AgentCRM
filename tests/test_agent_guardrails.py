from app.agent.agent_guardrails import (
    enforce_agent_guardrails
)


def test_critical_never_auto_reply():

    classification = {
        "urgency": "Critical"
    }

    plan = [
        "search_knowledge_base",
        "send_auto_reply"
    ]

    filtered = enforce_agent_guardrails(
        classification,
        plan
    )

    assert "send_auto_reply" not in filtered
    assert "escalate_to_human" in filtered