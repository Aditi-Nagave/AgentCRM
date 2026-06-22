from app.agent.planner import build_plan


def test_karen_refund_review_threat():

    classification = {
        "category": "Customer Churn Risk",
        "urgency": "High"
    }

    plan = build_plan(classification)

    assert "search_knowledge_base" in plan
    assert "get_contact_profile" in plan
    assert "scrape_public_sentiment" in plan
    assert "draft_reply" in plan
    assert "escalate_to_human" in plan

    assert len(plan) <= 6