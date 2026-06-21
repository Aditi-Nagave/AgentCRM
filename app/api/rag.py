# app/api/rag.py
from fastapi import APIRouter

from app.rag.retriever import (
    search_policies
)

router = APIRouter()


@router.get("/rag/search")
def rag_search(q: str):

    return {

        "query": q,

        "results":
        search_policies(q)
    }