"""FastAPI dependency injection."""

from __future__ import annotations

from functools import lru_cache

from api.services.state import TassApiState


@lru_cache
def get_api_state() -> TassApiState:
    """Singleton API state for request handlers."""
    return TassApiState()
