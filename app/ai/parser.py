import json

def parse_llm_response(response_text):

    try:

        cleaned = response_text.strip()

        cleaned = cleaned.replace(
            "```json",
            ""
        )

        cleaned = cleaned.replace(
            "```",
            ""
        )

        cleaned = cleaned.strip()

        return json.loads(cleaned)

    except Exception as e:

        print("\nPARSER ERROR:")
        print(e)
        print("RAW RESPONSE:")
        print(response_text)

        return {
            "category":"Unknown",
            "sentiment":"Neutral",
            "urgency":"Low",
            "requires_human":False,
            "confidence":0.0,
            "is_security":False,
            "is_spam":False
        }