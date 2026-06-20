# app/ai/reply_generator.py
from groq import Groq

from app.core.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def generate_reply(
        subject,
        body,
        classification,
        action,
        knowledge
):

    prompt = f"""
You are a CRM assistant.

Customer Email:

Subject:
{subject}

Body:
{body}

Classification:

{classification}

Action:

{action}

Knowledge:

{knowledge}

Generate a professional email reply.

Return only the reply.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.3
    )

    return response.choices[0].message.content.strip()