# app/intelligence/cache_service.py
from datetime import datetime
from datetime import timedelta

from app.models.web_intelligence_cache import (
    WebIntelligenceCache
)


CACHE_HOURS = 6


def get_cached_result(
    db,
    entity
):

    row = db.query(
        WebIntelligenceCache
    ).filter(

        WebIntelligenceCache.target_entity
        == entity

    ).first()

    if not row:
        return None

    if row.expires_at < datetime.utcnow():
        return None

    return row.scraped_data


def save_cache(
    db,
    entity,
    source_url,
    data
):

    expiry = datetime.utcnow() + timedelta(hours=6)

    row = WebIntelligenceCache(

        target_entity=entity,

        source_url=source_url,

        scraped_data=data,

        scraped_at=datetime.utcnow(),

        expires_at=expiry
    )

    db.add(row)

    db.commit()