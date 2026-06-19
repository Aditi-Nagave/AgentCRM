# app/services/priority_service.py
def calculate_priority(
        urgency,
        is_security,
        is_spam
):

    score = 0

    if urgency == "Critical":
        score += 100

    elif urgency == "High":
        score += 70

    if is_security:
        score += 50

    if is_spam:
        score -= 100

    return score