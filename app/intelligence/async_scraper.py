# app/intelligence/async_scraper.py
import asyncio

from app.intelligence.scraper import (
    scrape_website
)

async def fetch_market_data(company):

    urls = [

        f"https://www.google.com/search?q={company}",

        f"https://news.google.com/search?q={company}"
    ]

    loop = asyncio.get_event_loop()

    tasks = [

        loop.run_in_executor(
            None,
            scrape_website,
            url
        )

        for url in urls
    ]

    return await asyncio.gather(
        *tasks
    )