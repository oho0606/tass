"""Redis-backed picks cache with JSON serialization.

Keys:
  tass:picks:{date}          → JSON blob (picks + blocked + metadata)
  tass:picks:latest_date     → date string of most recent picks

TTL: 6 hours (configurable via PICKS_CACHE_TTL_SECONDS env)
"""

from __future__ import annotations

import json
from datetime import date, datetime
from typing import Any

from api.cache.client import redis_delete, redis_get, redis_set
from engine.core.logging import get_logger

logger = get_logger(__name__)

_KEY_PREFIX = "tass:picks"
_LATEST_DATE_KEY = f"{_KEY_PREFIX}:latest_date"
_TTL = 6 * 3600  # 6 h


def _date_key(d: str | date) -> str:
    return f"{_KEY_PREFIX}:{d}"


def cache_picks(
    pick_date: str,
    picks: list[dict[str, Any]],
    gate_blocked: list[dict[str, Any]],
    metadata: dict[str, Any],
) -> bool:
    """Store picks in Redis. Returns True on success."""
    payload = json.dumps(
        {
            "pick_date": pick_date,
            "picks": picks,
            "gate_blocked": gate_blocked,
            **metadata,
        },
        ensure_ascii=False,
        default=str,
    )
    ok = redis_set(_date_key(pick_date), payload, ex=_TTL)
    if ok:
        redis_set(_LATEST_DATE_KEY, pick_date, ex=_TTL + 3600)
        logger.info("Redis: picks cached for {}", pick_date)
    return ok


def get_cached_picks(
    pick_date: str | None = None,
) -> dict[str, Any] | None:
    """Load picks from Redis for *pick_date* (or latest if None).

    Returns the full payload dict or None if not found.
    """
    if pick_date is None:
        pick_date = redis_get(_LATEST_DATE_KEY)
        if not pick_date:
            return None

    raw = redis_get(_date_key(pick_date))
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        logger.warning("Redis picks JSON decode error: {}", exc)
        return None


def invalidate_picks(pick_date: str | None = None) -> None:
    """Remove cached picks; also clears latest_date pointer if it matches."""
    latest = redis_get(_LATEST_DATE_KEY)
    target = pick_date or latest
    if target:
        redis_delete(_date_key(target))
    if latest and (pick_date is None or latest == pick_date):
        redis_delete(_LATEST_DATE_KEY)
    logger.info("Redis: picks cache invalidated for {}", target)
