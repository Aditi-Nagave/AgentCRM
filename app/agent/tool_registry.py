# app/agent/tool_registry.py
MAX_TOOL_CALLS = 6


def validate_plan(plan):

    if len(plan) > MAX_TOOL_CALLS:

        return plan[:MAX_TOOL_CALLS]

    return plan