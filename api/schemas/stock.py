"""Pydantic models for stock detail endpoints."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from api.schemas.common import DomainScoreView, GateReportItem


class StockMetaResponse(BaseModel):
    """Stock metadata for detail header."""

    symbol: str
    name: str
    market: str | None = None
    rank: int | None = None
    total_score: float | None = None
    max_score: float | None = None
    grade: str | None = None
    recommendation: str | None = None
    gate: str | None = None


class IndicatorBar(BaseModel):
    """Single OHLCV + indicator bar for charting."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    sma_20: float | None = None
    sma_60: float | None = None
    macd: float | None = None
    macd_signal: float | None = None
    macd_hist: float | None = None
    atr: float | None = None


class IndicatorsResponse(BaseModel):
    """Technical indicator time series (BFF chart view model)."""

    symbol: str
    name: str
    bars: list[IndicatorBar]
    meta: dict[str, Any] = Field(default_factory=dict)


class DomainsResponse(BaseModel):
    """Domain scores formatted for radar chart."""

    symbol: str
    name: str
    domains: list[DomainScoreView]
    radar: dict[str, float] = Field(
        description="Normalized 0-100 scores keyed by domain label for ECharts radar"
    )


class RulesResponse(BaseModel):
    """Rule pass/fail and gate deductions for Explainable AI."""

    symbol: str
    name: str
    passed_conditions: list[str] = Field(default_factory=list)
    failed_conditions: list[str] = Field(default_factory=list)
    gate_report: list[GateReportItem] = Field(default_factory=list)
    composite_breakdown: dict[str, Any] = Field(default_factory=dict)
    recommendation_reason: list[str] = Field(default_factory=list)
