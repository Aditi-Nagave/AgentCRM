# app/services/security_detector.py
SECURITY_KEYWORDS = [
    "data breach",
    "ransomware",
    "suspicious login",
    "btc",
    "dark web",
    "security"
]

def detect_security(text):

    text = text.lower()

    for keyword in SECURITY_KEYWORDS:

        if keyword in text:
            return True

    return False