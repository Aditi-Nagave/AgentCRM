# app/services/knowledge_service.py
from pathlib import Path

KNOWLEDGE_DIR = Path("app/knowledge")


def load_all_policies():

    knowledge = ""

    for file in KNOWLEDGE_DIR.glob("*.md"):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            knowledge += f.read()

            knowledge += "\n\n"

    return knowledge