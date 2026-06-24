from app.background.email_tasks import analyze_email_task

result = analyze_email_task.delay(
    "Refund Request",
    "I want a refund"
)

print(result.get(timeout=10))