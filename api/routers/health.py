"""Health check router."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from api.deps import get_api_state
from api.schemas.common import HealthResponse
from api.services.state import TassApiState

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check(state: TassApiState = Depends(get_api_state)) -> HealthResponse:
    """Return API and engine health status including DB and Redis connectivity."""
    from api.cache.client import is_redis_available
    from api.db.session import is_db_available

    return HealthResponse(
        status="ok",
        service="tass-api",
        engine_version="1.0.0",
        mvp_mode=state.settings.mvp_mode,
        picks_cached=state.is_cached,
        db_connected=is_db_available(),
        redis_connected=is_redis_available(),
    )
