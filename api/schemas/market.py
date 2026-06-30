"""Pydantic models for market status streaming."""

from __future__ import annotations

from pydantic import BaseModel, Field


class MarketStatusEvent(BaseModel):
    """Real-time market status pushed via SSE/WebSocket."""

    event: str = Field(default="market_status")
    timestamp: str
    kospi_trend: str
    kosdaq_trend: str
    market_trend: str
    regime: str = Field(description="Bull / Bear / Neutral classification for UI")
    picks_date: str | None = None
    picks_count: int = 0
