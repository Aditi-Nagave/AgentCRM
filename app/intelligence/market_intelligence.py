# app/intelligence/market_intelligence.py
import asyncio

from app.intelligence.async_scraper import (
    fetch_market_data
)

from app.intelligence.sentiment_summary import (
    summarize_reviews
)

def build_market_intelligence(
    company
):

    results = asyncio.run(

        fetch_market_data(
            company
        )

    )

    return {

        "company":company,

        "sources":results,

        "summary":
        summarize_reviews(
            results
        )
    }