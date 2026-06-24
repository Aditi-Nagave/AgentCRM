# app/ai/classifier.py
from groq import Groq

from app.core.config import settings
from app.ai.prompts import CLASSIFICATION_PROMPT
from app.ai.parser import parse_llm_response

client = Groq(
    api_key=settings.GROQ_API_KEY
)

def classify_email(subject, body,thread_context,knowledge):

    email_text = f"""
        Subject: {subject}

        Body:{body}
    """

    prompt = CLASSIFICATION_PROMPT.format(
        email=email_text,
        thread_context=thread_context,
        knowledge=knowledge
    )

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0
    )

    content = response.choices[0].message.content

    print("\n====== GROQ RESPONSE ======")
    print(content)
    print("===========================\n")

    parsed = parse_llm_response(content)

    print("\nPARSED RESPONSE:")
    print(parsed)

    return parsed