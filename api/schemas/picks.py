"""Pydantic models for picks and ranking endpoints."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from api.schemas.common import PaginationMeta


class PickSummary(BaseModel):
    """Compact pick card for lists."""

    rank: int
    symbol: str
    name: str
    total_score: float
    max_score: float
    grade: str | None = None
    confidence: float | None = None
    confidence_stars: str | None = None
    risk: float | None = None
    risk_level: str | None = None
    probability: float | None = None
    recommendation: str | None = None
    recommendation_grade: str | None = None
    gate: str


class PickDetail(BaseModel):
    """Full pick payload for stock detail / explainable AI."""

    rank: int
    symbol: str
    name: str
    total_score: float
    max_score: float
    domains: dict[str, Any]
    confidence: float | None = None
    risk: float | None = None
    reasons: list[str] = Field(default_factory=list)
    gate: str
    grade: str | None = None
    probability: float | None = None
    probability_grade: str | None = None
    probability_level: str | None = None
    confidence_grade: str | None = None
    confidence_level: str | None = None
    confidence_stars: str | None = None
    risk_grade: str | None = None
    risk_grade_stars: str | None = None
    risk_level: str | None = None
    risk_decision: str | None = None
    risk_breakdown: list[dict[str, Any]] | None = None
    recommendation: str | None = None
    recommendation_grade: str | None = None
    recommendation_reason: list[str] | None = None
    passed_conditions: list[str] | None = None
    failed_conditions: list[str] | None = None
    gate_report: list[dict[str, Any]] | None = None
    composite_breakdown: dict[str, Any] | None = None


class DailyPicksResponse(BaseModel):
    """Today's Top 20 picks response."""

    date: str
    mvp_mode: bool
    generated_at: str
    universe_size: int
    candidates_evaluated: int
    picks: list[PickDetail]
    gate_blocked: list[PickDetail] = Field(default_factory=list)


class PicksHistoryItem(BaseModel):
    """Compact metadata for historical daily picks files."""

    date: str
    generated_at: str
    mvp_mode: bool
    universe_size: int
    candidates_evaluated: int
    picks_count: int
    gate_blocked_count: int
    top_symbols: list[str] = Field(default_factory=list)


class PicksHistoryResponse(BaseModel):
    """Recent picks history list for dashboard."""

    items: list[PicksHistoryItem]


class RankingResponse(BaseModel):
    """Paginated full-universe ranking."""

    date: str
    generated_at: str
    pagination: PaginationMeta
    items: list[PickSummary]
