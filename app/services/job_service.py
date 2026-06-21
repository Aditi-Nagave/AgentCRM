# app/services/job_service.py
import uuid

jobs = {}


def create_job():

    job_id = str(
        uuid.uuid4()
    )

    jobs[job_id] = {
        "status": "processing"
    }

    return job_id


def update_job(
    job_id,
    status
):
    if job_id in jobs:

        jobs[job_id]["status"] = status


def get_job_status(
    job_id
):
    return jobs.get(
        job_id,
        {
            "status": "not_found"
        }
    )