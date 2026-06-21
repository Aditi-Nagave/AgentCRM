# app/api/agent.py
from fastapi import APIRouter

router = APIRouter()


@router.post(
    "/agent/dry-run/{email_id}"
)
def dry_run(email_id: int):

    return {

        "email_id": email_id,

        "plan": [

            "search_knowledge_base",

            "escalate_to_human",

            "create_internal_ticket"
        ],

        "executed": False
    }