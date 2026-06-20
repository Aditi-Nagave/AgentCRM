# app/ai/prompts.py
CLASSIFICATION_PROMPT = """
You are an enterprise CRM analyst.

Company Policies:

{knowledge}

--------------------------------

Previous Conversation History:

{thread_context}

--------------------------------

Current Email:

{email}

--------------------------------

Analyze the CURRENT email using:

1. Email content
2. Thread history
3. Company policies

Return ONLY valid JSON.

Rules:

requires_human must be boolean:
true or false

is_security must be boolean:
true or false

is_spam must be boolean:
true or false

confidence must be a decimal number:
0.0 to 1.0

Required fields:

category
sentiment
urgency
requires_human
confidence
is_security
is_spam
customer_stage
recommended_action
"""