# app/services/intelligence_engine.py
from app.ai.classifier import classify_email

from app.services.context_builder import (
    get_thread_context,
    build_llm_context
)

from app.rag.retriever import (
    retrieve_knowledge
)

from app.services.action_engine import (
    process_action_engine
)
from app.services.internal_detector import (
    is_internal_email
)

from app.services.sentiment_service import (
analyze_sentiment
)

from app.agent.planner import build_plan

from app.agent.executor import execute_plan

from app.services.spam_detector import detect_spam
from app.services.security_detector import detect_security
from app.services.urgency_detector import detect_urgency


def process_email(
        db,
        sender,
        thread_id,
        subject,
        body
):

    try:
        if is_internal_email(sender):
            return { 
                "category": "Internal",
                "sentiment": "Neutral", 
                "sentiment_score": 0, 
                "urgency": "Low", 
                "requires_human": False, 
                "confidence": 1.0, 
                "is_security": False, 
                "is_spam": False, 
                "customer_stage": "Internal", 
                "recommended_action": "Route Internal Inbox", 
                "draft_reply": "", "agent_logs": []
                  }

        history = get_thread_context(
            db,
            thread_id
        )

        context = build_llm_context(
            history
        )
        print(context)
        query = f"""
            Subject:{subject}
            Body:{body}
        """

        knowledge = retrieve_knowledge(
                  query
        )

        sentiment_data = analyze_sentiment( body )

        classification = classify_email(
            subject,
            body,
            context,
            knowledge
        )

        classification[ "sentiment_score" ] = sentiment_data["score"]

        if classification["confidence"] < 0.70: 
            classification[ "requires_human" ] = True 
            classification[ "escalation_reason" ] = "Low Confidence Classification"

        plan = build_plan(
               classification
        )

        agent_logs = execute_plan(
            subject,
            body,
            plan
        )

        classification["agent_logs"] = agent_logs

        action_data = process_action_engine(
               subject,
               body,
               classification,
            knowledge
        )

        classification.update(
            action_data
        )

        return classification

    except Exception as e:

        print("\n===================")
        print("CLASSIFIER FAILED")
        print(type(e))
        print(e)
        print("===================\n")

        text = subject + " " + body

        sentiment_data = analyze_sentiment( body )

        return {

            "category":"Unknown",

            "sentiment": sentiment_data["label"],

            "sentiment_score": sentiment_data["score"],

            "urgency": detect_urgency(text),

            "requires_human":False,

            "confidence":0.0,

            "is_security":detect_security(text),

            "is_spam":detect_spam(sender, subject, body),

            "customer_stage":"Unknown",

            "recommended_action":"Manual Review Required",

            "draft_reply":"Thank you for contacting us. Your request has been received and will be reviewed shortly.",

            "agent_logs": []
        }  