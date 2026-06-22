from app.agent.planner import build_plan


def test_gdpr_request_workflow():

    classification = {
        "category": "GDPR Article 20 Request",
        "urgency": "High"
    }

    plan = build_plan(classification)

    expected_steps = [
        "search_knowledge_base",
        "get_thread_history",
        "flag_for_legal",
        "create_internal_ticket",
        "generate_gdpr_acknowledgement",
        "escalate_to_human"
    ]

    for step in expected_steps:
        assert step in plan

    assert len(plan) <= 6