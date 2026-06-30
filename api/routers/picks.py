"""Today's picks router."""

from __future__ import annotations

import json
from pathlib import Path

from fastapi import APIRouter, Depends, Query

from api.deps import get_api_state
from api.schemas.picks import DailyPicksResponse, PickDetail, PicksHistoryItem, PicksHistoryResponse
from api.services.state import TassApiState, pick_detail_from_result

router = APIRouter(tags=["picks"])


@router.get("/picks/today", response_model=DailyPicksResponse)
def today_picks(
    refresh: bool = Query(False, description="Force regenerate picks from engine"),
    state: TassApiState = Depends(get_api_state),
) -> DailyPicksResponse:
    """Return Today's Top 20 ranked picks (BFF view model)."""
    cache = state.ensure_picks(refresh=refresh)
    picks = [pick_detail_from_result(p) for p in cache.picks]
    return DailyPicksResponse(
        date=cache.date,
        mvp_mode=cache.mvp_mode,
        generated_at=cache.generated_at,
        universe_size=cache.universe_size,
        candidates_evaluated=cache.candidates_evaluated,
        picks=picks,
        gate_blocked=[pick_detail_from_result(p) for p in cache.gate_blocked],
    )


@router.get("/picks/history", response_model=PicksHistoryResponse)
def picks_history(
    limit: int = Query(7, ge=1, le=30, description="Number of recent days to return"),
    state: TassApiState = Depends(get_api_state),
) -> PicksHistoryResponse:
    """Return recent picks history from output JSON snapshots."""
    output_dir = Path("output")
    items: list[PicksHistoryItem] = []
    if not output_dir.exists():
        return PicksHistoryResponse(items=items)

    files = sorted(output_dir.glob("picks_*.json"), reverse=True)
    for path in files:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        picks = payload.get("picks") or []
        gate_blocked = payload.get("gate_blocked") or []
        symbols = [
            str(pick.get("symbol", "")).strip()
            for pick in picks[:3]
            if str(pick.get("symbol", "")).strip()
        ]
        items.append(
            PicksHistoryItem(
                date=str(payload.get("date", "")),
                generated_at=str(payload.get("generated_at", "")),
                mvp_mode=bool(payload.get("mvp_mode", state.settings.mvp_mode)),
                universe_size=int(payload.get("universe_size", 0)),
                candidates_evaluated=int(payload.get("candidates_evaluated", 0)),
                picks_count=len(picks),
                gate_blocked_count=len(gate_blocked),
                top_symbols=symbols,
            )
        )
        if len(items) >= limit:
            break
    return PicksHistoryResponse(items=items)
