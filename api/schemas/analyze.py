"""Pydantic models for analyze workflow endpoints."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from api.schemas.common import DomainScoreView
from api.schemas.picks import PickDetail


class AnalysisMode(str, Enum):
    """Analysis timing basis (maps to recommendation_v1.yaml on backend)."""

    close = "close"
    open = "open"
    intraday = "intraday"


class AnalyzeRequest(BaseModel):
    mode: AnalysisMode = AnalysisMode.close


class AnalyzeTriggerResponse(BaseModel):
    job_id: str


class AnalyzeStatusEvent(BaseModel):
    job_id: str
    status: str
    phase: str
    progress: int = Field(..., ge=0, le=100)
    message: str
    error: str | None = None
    summary: dict[str, Any] | None = None
    picks: list[PickDetail] | None = None
    gate_blocked: list[PickDetail] | None = None


class AnalyzeSummary(BaseModel):
    universe_size: int
    passed_count: int
    elapsed_seconds: float
    analysis_mode: str
    date: str
    generated_at: str


class RuleAccordionItem(BaseModel):
    title: str
    score_delta: float | None = None
    detail: str
    passed: bool = True


class PenaltyItem(BaseModel):
    title: str
    score_delta: float | None = None
    detail: str


class AnalysisDetailResponse(BaseModel):
    symbol: str
    name: str
    rank: int | None = None
    total_score: float
    max_score: float
    recommendation: str | None = None
    summary: str
    radar: dict[str, float] = Field(default_factory=dict)
    domains: list[DomainScoreView] = Field(default_factory=list)
    rules: list[RuleAccordionItem] = Field(default_factory=list)
    penalties: list[PenaltyItem] = Field(default_factory=list)
