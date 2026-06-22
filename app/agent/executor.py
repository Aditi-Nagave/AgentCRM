# app/agent/executor.py
from app.agent.tools import *

from app.agent.logger import create_log

from app.agent.tool_registry import (
    MAX_TOOL_CALLS
)

from app.services.audit_logger import (
    create_audit_log
)

def execute_plan(
    db,
    subject,
    sender,
    plan
):
    logs = []
    tool_count = 0

    for step in plan:

        tool_count += 1

        if tool_count > MAX_TOOL_CALLS:
            break

        if step == "search_knowledge_base":

            result = search_knowledge_base(subject)

            logs.append(
                create_log(
                    "Need policy information",
                    step,
                    str(result),
                    "Continue"
                )
            )

        elif step == "get_contact_profile":

            result = get_contact_profile(sender)

            logs.append(
                create_log(
                    "Need CRM profile",
                    step,
                    str(result),
                    "Continue"
                )
            )

        elif step == "check_account_status":

            result = check_account_status(sender)

            logs.append(
                create_log(
                    "Need account info",
                    step,
                    str(result),
                    "Continue"
                )
            )

        elif step == "escalate_to_human":

            result = escalate_to_human(subject)

            create_audit_log(

                  db,

                 "email",

                  subject,

                 "ESCALATED_TO_HUMAN"
            )

            logs.append(
                create_log(
                    "Human intervention required",
                    step,
                    str(result),
                    "Stop"
                )
            )

        elif step == "create_internal_ticket":

            result = create_internal_ticket(subject)

            create_audit_log(

                 db,

                 "email",

                 subject,
 
                 "INTERNAL_TICKET_CREATED"
            )

            logs.append(
                create_log(
                    "Need engineering review",
                    step,
                    str(result),
                    "Stop"
                )
            )

        elif step == "get_thread_history":

            result = get_thread_history(
                subject
            )

            logs.append(
                create_log(
                    "Need thread history",
                    step,
                    str(result),
                    "Continue"
                )
            )

        elif step == "draft_reply":

            result = draft_reply(
                subject
            )

            logs.append(
                create_log(
                    "Prepare customer reply",
                    step,
                    str(result),
                    "Continue"
                )
            )

        elif step == "flag_for_legal":

            result = flag_for_legal(
                subject
            )

            create_audit_log(

                 db,

                 "email",

                 subject,

                 "LEGAL_FLAGGED"
            )

            logs.append(
                create_log(
                    "Legal review required",
                    step,
                    str(result),
                    "Continue"
                )
            )

        elif step == "send_auto_reply":

            result = send_auto_reply(
                sender
            )
            
            create_audit_log(

                    db,

                    "email",

                    sender,

                    "AUTO_REPLY_SENT"
            )
            
            logs.append(
                create_log(
                    "Send automated reply",
                    step,
                    str(result),
                    "Stop"
                )
            )

        elif step == "scrape_public_sentiment":
            company = "SenAI"

            result = scrape_public_sentiment(
                db,
                company
            )

            logs.append(
                create_log(
                    "Need reputation data",
                    step,
                    str(result),
                    "Continue"
                )
            )

        elif step == "generate_gdpr_acknowledgement":

            result = generate_gdpr_acknowledgement()

            logs.append(
                create_log(
                    "Prepare GDPR acknowledgement",
                    step,
                    str(result),
                    "Continue"
                )
            )


    return logs