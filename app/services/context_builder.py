# app/services/context_builder.py
from app.models.email import Email


def get_thread_context(
        db,
        thread_id,
        limit=10
):
    emails = (
        db.query(Email)
        .filter(
            Email.thread_id == thread_id
        )
        .order_by(Email.timestamp)
        .limit(limit)
        .all()
    )

    return emails


def build_llm_context(
        thread_emails
):
    if not thread_emails:
        return "No previous thread history."

    context = ""

    for email in thread_emails:

        context += f"""

Sender: {email.sender}

Subject: {email.subject}

Body:
{email.body}

Category: {email.category}

Urgency: {email.urgency}

--------------------------------
"""

    return context