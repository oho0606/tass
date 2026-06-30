"""Full ranking router with pagination."""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query

from api.deps import get_api_state
from api.schemas.common import PaginationMeta
from api.schemas.picks import RankingResponse
from api.services.state import TassApiState, paginate, pick_summary_from_result

router = APIRouter(tags=["ranking"])


@router.get("/ranking", response_model=RankingResponse)
def ranking(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    refresh: bool = Query(False),
    state: TassApiState = Depends(get_api_state),
) -> RankingResponse:
    """Return paginated full-universe ranking."""
    cache = state.ensure_picks(refresh=refresh)
    items = [pick_summary_from_result(p) for p in cache.all_ranked]
    page_items, total, total_pages = paginate(items, page, page_size)
    return RankingResponse(
        date=cache.date,
        generated_at=cache.generated_at,
        pagination=PaginationMeta(
            page=page,
            page_size=page_size,
            total=total,
            total_pages=total_pages,
        ),
        items=page_items,
    )
