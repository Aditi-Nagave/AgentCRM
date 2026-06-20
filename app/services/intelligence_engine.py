# app/services/intelligence_engine.py
from app.ai.classifier import classify_email

from app.services.context_builder import (
    get_thread_context,
    build_llm_context
)

from app.rag.retriever import (
    retrieve_knowledge
)

from app.services.spam_detector import detect_spam
from app.services.security_detector import detect_security
from app.services.urgency_detector import detect_urgency


def process_email(
        db,
        thread_id,
        subject,
        body
):

    try:

        history = get_thread_context(
            db,
            thread_id
        )

        context = build_llm_context(
            history
        )

        query = f"""
            Subject:{subject}
            Body:{body}
        """

        knowledge = retrieve_knowledge(
                  query
        )

        return classify_email(
            subject,
            body,
            context,
            knowledge
        )

    except Exception as e:

        print("\n===================")
        print("CLASSIFIER FAILED")
        print(type(e))
        print(e)
        print("===================\n")

        text = subject + " " + body

        return {

            "category":"Unknown",

            "sentiment":"Neutral",

            "urgency":detect_urgency(text),

            "requires_human":False,

            "confidence":0,

            "is_security":detect_security(text),

            "is_spam":detect_spam(subject, body),

            "customer_stage":"Unknown",

            "recommended_action":"Manual Review Required"
        }