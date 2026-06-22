# app/core/exceptions.py
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import (
    RequestValidationError
)

from sqlalchemy.exc import SQLAlchemyError

async def value_error_handler(
    request: Request,
    exc: ValueError
):

    return JSONResponse(

        status_code=400,

        content={
            "error_code":
            "VALIDATION_ERROR",

            "message":
            str(exc),

            "details":
            None
        }
    )

async def validation_error_handler(
    request,
    exc
):

    return JSONResponse(

        status_code=422,

        content={

            "error_code":
            "REQUEST_VALIDATION_ERROR",

            "message":
            "Invalid Request",

            "details":
            exc.errors()
        }
    )

async def database_error_handler(
    request,
    exc
):

    return JSONResponse(

        status_code=500,

        content={

            "error_code":
            "DATABASE_ERROR",

            "message":
            "Database Operation Failed",

            "details": {}
        }
    )

async def generic_error_handler(
    request,
    exc
):

    return JSONResponse(

        status_code=500,

        content={

            "error_code":
            "INTERNAL_SERVER_ERROR",

            "message":
            str(exc),

            "details": {}
        }
    )

