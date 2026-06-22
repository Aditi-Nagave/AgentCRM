# app/main.py
from fastapi import FastAPI

from app.api.ingest import router as ingest_router
from app.api.threads import router as thread_router
from app.api.dashboard import router as dashboard_router
from app.api.rag import (router as rag_router)
from app.api.agent import (router as agent_router)
from app.api.status import (router as status_router)
from app.api.analytics import (router as analytics_router)
from app.api.respond import router as respond_router
from app.api.drafts import router as drafts_router
from app.api.contacts import router as contacts_router
from app.api.audit import router as audit_router
from app.api.intelligence import router as intelligence_router
from app.api.category_analytics import router as category_router


from app.models.audit_log import AuditLog
from app.models.knowledge_chunk import KnowledgeChunk
from app.models.web_intelligence_cache import WebIntelligenceCache
from app.models.contact import Contact
from app.models.thread import Thread
from app.models.email import Email
from app.models.action import Action


from app.core.exceptions import (
    value_error_handler,
    validation_error_handler,
    database_error_handler,
    generic_error_handler
)

from fastapi.exceptions import (
    RequestValidationError
)

from sqlalchemy.exc import (
    SQLAlchemyError
)

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
app.include_router(respond_router)
app.include_router(drafts_router)
app.include_router(contacts_router)
app.include_router(audit_router)
app.include_router(intelligence_router)
app.include_router(category_router)
app.add_exception_handler(ValueError, value_error_handler)
app.add_exception_handler(RequestValidationError, validation_error_handler)
app.add_exception_handler(SQLAlchemyError,database_error_handler)
app.add_exception_handler(Exception,generic_error_handler)

@app.get("/")
def home():

    return {
        "message": "AI CRM Running"
    }