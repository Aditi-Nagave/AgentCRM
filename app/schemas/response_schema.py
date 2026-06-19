# app/schemas/response_schema.py
from pydantic import BaseModel

class ApiResponse(BaseModel):

    status: str
    message: str