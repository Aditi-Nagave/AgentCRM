# app/services/thread_service.py
from app.models.thread import Thread

def create_thread_if_not_exists(
    db,
    thread_id,
    subject,
    sender
):

    thread = db.query(Thread).filter(
        Thread.thread_id == thread_id
    ).first()

    if not thread:

        thread = Thread(
            thread_id=thread_id,
            subject=subject,
            sender_email=sender
        )

        db.add(thread)
        db.commit()

    return thread