# app/agent/executor.py
from app.agent.tools import *

from app.agent.logger import create_log


def execute_plan(

        subject,

        sender,

        plan
):

    logs = []

    for step in plan:

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

            logs.append(

                create_log(

                    "Need engineering review",

                    step,

                    str(result),

                    "Stop"
                )
            )

    return logs