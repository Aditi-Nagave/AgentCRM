from app.agent.planner import build_plan


def test_bob_sla_breach_workflow():

    classification = {
        "category": "SLA Breach",
        "urgency": "High"
    }

    plan = build_plan(classification)

    expected_steps = [
        "get_thread_history",
        "search_knowledge_base",
        "check_account_status",
        "flag_for_legal",
        "draft_reply",
        "escalate_to_human"
    ]

    for step in expected_steps:
        assert step in plan

    assert len(plan) <= 6