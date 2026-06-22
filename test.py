from app.agent.planner import (
    build_plan
)

print("\n=== SECURITY TEST ===\n")

classification = {

    "category":
    "Security Incident",

    "urgency":
    "Critical"
}

plan = build_plan(
    classification
)

print("Generated Plan:")

for step in plan:

    print("-", step)

passed = True

if "escalate_to_human" not in plan:

    passed = False

if "create_internal_ticket" not in plan:

    passed = False

if "send_auto_reply" in plan:

    passed = False

if passed:

    print(
        "\n✅ Security Test PASSED"
    )

else:

    print(
        "\n❌ Security Test FAILED"
    )