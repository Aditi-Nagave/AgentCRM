# app/ai/parser.py
import json

print("PARSER FILE LOADED")

def convert_bool(value):

    if isinstance(value, bool):
        return value

    if isinstance(value, str):

        value = value.strip().lower()

        return value in [
            "yes",
            "true",
            "y"
        ]

    return False


def convert_confidence(value):

    if isinstance(value, (int, float)):
        return float(value)

    if isinstance(value, str):

        value = value.strip().lower()

        mapping = {
            "very high": 0.99,
            "high": 0.90,
            "medium": 0.70,
            "low": 0.50
        }

        if value in mapping:
            return mapping[value]

        try:
            return float(value)

        except:
            return 0.0

    return 0.0


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

        start = cleaned.find("{")
        end = cleaned.rfind("}")

        if start != -1 and end != -1:
            cleaned = cleaned[start:end+1]

        data = json.loads(cleaned)

        data["requires_human"] = convert_bool(
            data.get("requires_human")
        )

        data["is_security"] = convert_bool(
            data.get("is_security")
        )

        data["is_spam"] = convert_bool(
            data.get("is_spam")
        )

        data["confidence"] = convert_confidence(
            data.get("confidence")
        )

        return data

    except Exception as e:

        print("\nPARSER ERROR:")
        print(e)

        return {

            "category":"Unknown",

            "customer_stage":"Unknown",

            "sentiment":"Neutral",

            "urgency":"Low",

            "requires_human":False,

            "confidence":0.0,

            "is_security":False,

            "is_spam":False,

            "recommended_action":"Review Required"
        }