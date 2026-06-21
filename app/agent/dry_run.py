# app/agent/dry_run.py
from app.agent.planner import build_plan


def run_dry_run(classification):

    return {

        "executed": False,

        "plan": build_plan(classification)
    }