# app/ai/prompts.py
CLASSIFICATION_PROMPT = """
You are an enterprise CRM analyst.

Analyze the email.

Classify:

1. category
2. sentiment
3. urgency
4. requires_human
5. confidence
6. is_security
7. is_spam

Possible Categories:

- Complaint
- Refund
- Security
- Billing
- Sales
- GDPR
- Legal
- Technical Support
- General Inquiry

Urgency:

- Low
- Medium
- High
- Critical

Return ONLY JSON.

EMAIL:

{email}
"""