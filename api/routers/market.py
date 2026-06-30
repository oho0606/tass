"""Market status SSE and WebSocket streaming."""

from __future__ import annotations

import asyncio
import json

from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from starlette.responses import StreamingResponse

from api.deps import get_api_state
from api.schemas.market import MarketStatusEvent
from api.services.state import TassApiState

router = APIRouter(tags=["market"])


def _build_event(state: TassApiState) -> MarketStatusEvent:
    data = state.market_status()
    return MarketStatusEvent(
        timestamp=data["timestamp"],
        kospi_trend=data["kospi_trend"],
        kosdaq_trend=data["kosdaq_trend"],
        market_trend=data["market_trend"],
        regime=data["regime"],
        picks_date=data.get("picks_date"),
        picks_count=int(data.get("picks_count", 0)),
    )


@router.get("/ws/market")
async def market_sse(state: TassApiState = Depends(get_api_state)) -> StreamingResponse:
    """Server-Sent Events stream for market status (lightweight push)."""

    async def event_stream():
        while True:
            event = _build_event(state)
            yield f"data: {event.model_dump_json()}\n\n"
            await asyncio.sleep(5)

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@router.websocket("/ws/market/ws")
async def market_websocket(websocket: WebSocket) -> None:
    """WebSocket alternative for market status."""
    await websocket.accept()
    state = get_api_state()
    try:
        while True:
            event = _build_event(state)
            await websocket.send_text(event.model_dump_json())
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        return
