from app.agent.planner import build_plan


def test_ransomware_security_incident():

    classification = {
        "category": "Ransomware",
        "urgency": "Critical"
    }

    plan = build_plan(classification)

    assert "search_knowledge_base" in plan
    assert "get_thread_history" in plan
    assert "check_account_status" in plan
    assert "escalate_to_human" in plan
    assert "create_internal_ticket" in plan

    # Critical emails must never auto reply
    assert "send_auto_reply" not in plan

    assert len(plan) <= 6