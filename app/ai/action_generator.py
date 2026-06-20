# app/ai/action_generator.py
from groq import Groq

from app.core.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def generate_action(
        classification,
        knowledge
):

    prompt = f"""
You are a CRM Action Engine.

Classification:

{classification}

Knowledge:

{knowledge}

Return ONLY the best next action.

Examples:

Escalate to Manager

Escalate to Security Team

Send Pricing Details

Schedule Sales Call
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    return response.choices[0].message.content.strip()