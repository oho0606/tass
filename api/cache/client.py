"""Redis client with graceful fallback (no-op when Redis is not configured)."""

from __future__ import annotations

import threading
from typing import Any

from engine.core.logging import get_logger

logger = get_logger(__name__)

_lock = threading.Lock()
_client = None
_redis_available: bool | None = None  # None = not yet checked


def _build_client():
    """Connect to Redis; return None if not configured or unreachable."""
    try:
        import redis

        from config.app_settings import get_settings

        settings = get_settings()
        url = settings.redis_url.strip()

        if not url:
            return None

        r = redis.from_url(url, decode_responses=True, socket_connect_timeout=3)
        r.ping()
        return r
    except Exception as exc:
        logger.info("Redis not available ({}), using in-memory fallback", exc)
        return None


def _ensure_client():
    global _client, _redis_available
    with _lock:
        if _redis_available is not None:
            return _client
        _client = _build_client()
        _redis_available = _client is not None
        if _redis_available:
            logger.info("Redis connected")
        return _client


def is_redis_available() -> bool:
    """Return True if Redis is configured and reachable."""
    _ensure_client()
    return bool(_redis_available)


def get_client():
    """Return raw Redis client or None."""
    return _ensure_client()


def redis_get(key: str) -> str | None:
    """Get a string value; return None on any failure."""
    r = _ensure_client()
    if r is None:
        return None
    try:
        return r.get(key)
    except Exception as exc:
        logger.warning("Redis GET {} failed: {}", key, exc)
        return None


def redis_set(key: str, value: str, ex: int | None = None) -> bool:
    """Set a string value with optional TTL (seconds). Return True on success."""
    r = _ensure_client()
    if r is None:
        return False
    try:
        r.set(key, value, ex=ex)
        return True
    except Exception as exc:
        logger.warning("Redis SET {} failed: {}", key, exc)
        return False


def redis_delete(key: str) -> None:
    r = _ensure_client()
    if r is None:
        return
    try:
        r.delete(key)
    except Exception as exc:
        logger.warning("Redis DEL {} failed: {}", key, exc)


def redis_hgetall(key: str) -> dict[str, Any]:
    r = _ensure_client()
    if r is None:
        return {}
    try:
        return r.hgetall(key) or {}
    except Exception as exc:
        logger.warning("Redis HGETALL {} failed: {}", key, exc)
        return {}


def redis_hset(key: str, mapping: dict[str, Any], ex: int | None = None) -> bool:
    r = _ensure_client()
    if r is None:
        return False
    try:
        r.hset(key, mapping=mapping)
        if ex:
            r.expire(key, ex)
        return True
    except Exception as exc:
        logger.warning("Redis HSET {} failed: {}", key, exc)
        return False
