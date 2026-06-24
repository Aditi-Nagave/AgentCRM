# app/services/intelligence_engine.py
from app.ai.classifier import classify_email

from app.services.context_builder import (
    get_thread_context,
    build_llm_context
)
import traceback

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

from app.rag.citation_helper import (
    format_citations
)

from app.intelligence.trigger_detector import (
    should_fetch_intelligence
)

from app.services.reputation_service import (
    scrape_public_sentiment
)

from app.services.sentiment_trend_service import (
    has_unanswered_complaints
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
                "draft_reply": "Internal email received.", 
                "agent_logs": [

            {

                "thought":
                "Internal email detected",

                "action":
                "Route Internal Inbox",

                "observation":
                "Sender belongs to internal domain",

                "next_step":
                "No AI workflow required"

            }

        ]
                  }

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

        knowledge_results = retrieve_knowledge(
                query
        )

        knowledge = "\n\n".join(

             item["chunk"]

        for item in knowledge_results
        )

        policy_citations = format_citations(
              knowledge_results
        )

        sentiment_data = analyze_sentiment(body)

        market_context = ""

        if should_fetch_intelligence(
                    "",
                    "",
                    sentiment_data["score"],
                    subject,
                    body
            ):
            intel = scrape_public_sentiment(
                      db,
                     "SenAI"
                )

            market_context = str(intel)

        knowledge += f"""

        MARKET INTELLIGENCE

           {market_context}
                 """

        classification = classify_email(
              subject,
               body,
              context,
               knowledge
        )
        classification["policy_citations"] = policy_citations
        classification[ "sentiment_score" ] = sentiment_data["score"]

        if has_unanswered_complaints(db,sender):
            classification["category"] = (
            "Customer Churn Risk"
    )

        if classification["confidence"] < 0.70: 
            classification[ "requires_human" ] = True 
            classification[ "escalation_reason" ] = "Low Confidence Classification"

        plan = build_plan(
               classification
        )

        agent_logs = execute_plan(
            db,
            subject,
            sender,
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

        traceback.print_exc()

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