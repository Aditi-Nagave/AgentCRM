# app/agent/tools.py
from app.rag.retriever import search_policies


def search_knowledge_base(query):

    return search_policies(query)


def get_contact_profile(email):

    return {

        "email": email,

        "vip": False,

        "account_value": 1000,

        "churn_risk": "Low"
    }


def check_account_status(email):

    return {

        "tier": "Enterprise",

        "billing_status": "Active"
    }


def escalate_to_human(reason):

    return {

        "status": "Escalated",

        "reason": reason
    }


def create_internal_ticket(title):

    return {

        "status": "Created",

        "ticket": title
    }