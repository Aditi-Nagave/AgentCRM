# app/api/status.py
from fastapi import APIRouter

from app.services.job_service import (
    get_job_status
)

router = APIRouter()


@router.get(
    "/api/status/{job_id}"
)
def status(job_id: str):

    return get_job_status(
        job_id
    )