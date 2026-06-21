# app/main.py
from fastapi import FastAPI

from app.api.ingest import router as ingest_router
from app.api.threads import router as thread_router
from app.api.dashboard import router as dashboard_router
from app.api.rag import (router as rag_router)
from app.api.agent import (router as agent_router)

from app.core.database import Base
from app.core.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ingest_router)
app.include_router(thread_router)
app.include_router(dashboard_router)
app.include_router(rag_router)
app.include_router(agent_router)

@app.get("/")
def home():

    return {
        "message": "AI CRM Running"
    }