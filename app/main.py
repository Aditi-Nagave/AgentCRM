# app/main.py
from fastapi import FastAPI

from app.api.ingest import router as ingest_router
from app.api.threads import router as thread_router
from app.api.dashboard import router as dashboard_router
from app.api.rag import (router as rag_router)
from app.api.agent import (router as agent_router)
from app.api.status import (router as status_router)
from app.api.analytics import (router as analytics_router)
from app.core.exceptions import (value_error_handler)


from app.core.database import Base
from app.core.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ingest_router)
app.include_router(thread_router)
app.include_router(dashboard_router)
app.include_router(rag_router)
app.include_router(agent_router)
app.include_router(status_router)
app.include_router(analytics_router)
app.add_exception_handler(ValueError, value_error_handler)

@app.get("/")
def home():

    return {
        "message": "AI CRM Running"
    }