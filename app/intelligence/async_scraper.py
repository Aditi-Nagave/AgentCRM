# app/intelligence/async_scraper.py
import asyncio

from app.intelligence.scraper import (
    scrape_trustpilot
)


async def fetch_market_data(
    company
):

    loop = asyncio.get_event_loop()

    trustpilot = loop.run_in_executor(
        None,
        scrape_trustpilot,
        company
    )

    results = await asyncio.gather(
        trustpilot,
        return_exceptions=True
    )

    return results