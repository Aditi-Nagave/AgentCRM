from app.agent.planner import (
    build_plan
)

classification = {

    "category":
    "Customer Churn Risk",

    "urgency":
    "High"
}

print(
    build_plan(
        classification
    )
)