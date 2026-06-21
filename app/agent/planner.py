# app/agent/planner.py
from app.agent.tool_registry import (
    validate_plan
)


def build_plan(classification):

    category = classification["category"]

    urgency = classification["urgency"]

    plan = []

    # Security

    if category in [

        "Security Incident",

        "Data Breach",

        "Ransomware"
    ]:

        plan = [

            "search_knowledge_base",

            "get_thread_history",

            "check_account_status",

            "draft_reply",

            "escalate_to_human",

            "create_internal_ticket"
        ]

    # GDPR

    elif (

        "gdpr" in category.lower()

        or

        "article 20" in category.lower()
    ):

        plan = [

            "search_knowledge_base",

            "get_thread_history",

            "flag_for_legal",

            "draft_reply",

            "escalate_to_human"
        ]

    # Legal

    elif (

        "legal" in category.lower()

        or

        urgency == "Critical"
    ):

        plan = [

            "search_knowledge_base",

            "get_thread_history",

            "flag_for_legal",

            "draft_reply",

            "escalate_to_human"
        ]

    # Refund

    elif category == "Refund Request":

        plan = [

            "search_knowledge_base",

            "check_account_status",

            "draft_reply",

            "escalate_to_human"
        ]

    # Churn

    elif category == "Customer Churn Risk":

        plan = [

            "search_knowledge_base",

            "get_contact_profile",

            "scrape_public_sentiment",

            "draft_reply",

            "escalate_to_human"
        ]

    # Pricing

    elif category == "Pricing Inquiry":

        plan = [

            "search_knowledge_base",

            "get_contact_profile",

            "draft_reply"
        ]

    else:

        plan = [

            "search_knowledge_base",

            "draft_reply"
        ]

    return validate_plan(plan)