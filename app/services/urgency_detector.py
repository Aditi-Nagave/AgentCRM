# app/services/urgency_detector.py
CRITICAL = [
    "urgent",
    "p0",
    "legal",
    "ransomware",
    "cease and desist",
    "production down"
]

HIGH = [
    "refund",
    "deadline",
    "sla",
    "escalation"
]

def detect_urgency(text):

    text = text.lower()

    for word in CRITICAL:
        if word in text:
            return "Critical"

    for word in HIGH:
        if word in text:
            return "High"

    return "Low"