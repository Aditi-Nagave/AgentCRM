# app/services/reputation_service.py

from app.intelligence.market_intelligence import (
    build_market_intelligence
)

from app.intelligence.cache_service import (
    get_cached_result,
    save_cache
)


def scrape_public_sentiment(
    db,
    company
):

    cached = get_cached_result(
        db,
        company
    )

    if cached:
        return cached

    result = build_market_intelligence(
        company
    )

    save_cache(

        db,

        company,

        "trustpilot",

        result
    )

    return result
