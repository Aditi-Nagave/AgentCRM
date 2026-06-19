# app/ai/prompts.py
CLASSIFICATION_PROMPT = """
You are an enterprise CRM analyst.

Previous conversation history:

{thread_context}

--------------------------------

Current Email:

{email}

--------------------------------

Analyze the CURRENT email while considering
the conversation history.

Return ONLY a valid JSON object with these fields:

category
sentiment
urgency
requires_human
confidence
is_security
is_spam
customer_stage

customer_stage options:

- New Lead
- Evaluation
- Trial
- Existing Customer
- Expansion Opportunity
- Churn Risk
- Support Escalation
"""