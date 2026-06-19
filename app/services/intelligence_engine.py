# app/services/intelligence_engine.py
from app.ai.classifier import classify_email
from app.services.spam_detector import detect_spam
from app.services.security_detector import detect_security
from app.services.urgency_detector import detect_urgency


def process_email(subject, body):

    try:

        result = classify_email(
            subject,
            body
        )

        return result

    except Exception as e:

        print("\nCLASSIFIER FAILED:")
        print(e)

        text = subject + " " + body


        return {

            "category":"Unknown",

            "sentiment":"Neutral",

            "urgency":detect_urgency(text),

            "requires_human":False,

            "confidence":0.0,

            "is_security":detect_security(text),

            "is_spam":detect_spam(subject, body)
        }