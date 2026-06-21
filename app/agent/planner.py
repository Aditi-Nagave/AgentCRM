# app/agent/planner.py
def build_plan(classification):

    category = classification["category"]

    urgency = classification["urgency"]

    if category in [
        "Security Incident",
        "Data Breach",
        "Ransomware"
    ]:

        return [

            "search_knowledge_base",

            "escalate_to_human",

            "create_internal_ticket"
        ]

    if urgency in [
        "Critical",
        "High"
    ]:

        return [

            "search_knowledge_base",

            "escalate_to_human"
        ]

    if category == "Refund Request":

        return [

            "search_knowledge_base",

            "check_account_status",

            "escalate_to_human"
        ]

    if category == "Pricing Inquiry":

        return [

            "search_knowledge_base",

            "get_contact_profile"
        ]

    return [

        "search_knowledge_base"
    ]