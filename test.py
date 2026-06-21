from app.agent.planner import build_plan


def test_bob_sla_chain():

    plan = build_plan({

        "category": "SLA Breach",

        "urgency": "High"
    })

    expected = [

        "get_thread_history",

        "search_knowledge_base",

        "check_account_status",

        "flag_for_legal",

        "draft_reply",

        "escalate_to_human"
    ]

    if plan == expected:

        print("✅ Bob SLA Chain Test PASSED")

    else:

        print("❌ Bob SLA Chain Test FAILED")
        print("Expected:", expected)
        print("Got:", plan)


def test_gdpr_chain():

    plan = build_plan({

        "category":
        "GDPR Article 20 Request",

        "urgency":
        "High"
    })

    expected = [

        "search_knowledge_base",

        "get_thread_history",

        "flag_for_legal",

        "create_internal_ticket",

        "generate_gdpr_acknowledgement",

        "escalate_to_human"
    ]

    if plan == expected:

        print("✅ GDPR Workflow Test PASSED")

    else:

        print("❌ GDPR Workflow Test FAILED")
        print("Expected:", expected)
        print("Got:", plan)


def test_critical_never_auto_reply():

    plan = build_plan({

        "category":
        "Security Incident",

        "urgency":
        "Critical"
    })

    passed = (

        "send_auto_reply" not in plan

        and

        "escalate_to_human" in plan
    )

    if passed:

        print("✅ Critical Email Guardrail PASSED")

    else:

        print("❌ Critical Email Guardrail FAILED")
        print("Generated Plan:", plan)


if __name__ == "__main__":

    print("\n==============================")
    print("AUTONOMOUS AGENT ASSESSMENT")
    print("==============================\n")

    test_bob_sla_chain()

    test_gdpr_chain()

    test_critical_never_auto_reply()

    print("\n==============================")
    print("ASSESSMENT COMPLETE")
    print("==============================")