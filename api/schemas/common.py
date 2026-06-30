"""Shared Pydantic models for TASS API (TASS-040)."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """System health check payload."""

    status: str = Field(..., examples=["ok"])
    service: str = Field(..., examples=["tass-api"])
    engine_version: str
    mvp_mode: bool
    picks_cached: bool
    db_connected: bool = False
    redis_connected: bool = False


class PaginationMeta(BaseModel):
    """Pagination metadata."""

    page: int = Field(..., ge=1)
    page_size: int = Field(..., ge=1, le=100)
    total: int = Field(..., ge=0)
    total_pages: int = Field(..., ge=0)


class DomainScoreView(BaseModel):
    """BFF view model for a single domain score (radar chart)."""

    key: str
    label: str
    score: float
    max_score: float
    grade: str | None = None
    state: str | None = None
    status: str = "implemented"


class GateReportItem(BaseModel):
    """Gate evaluation row for Explainable AI."""

    gate_key: str | None = None
    gate_name: str | None = None
    status: str
    threshold: str | None = None
    actual: str | None = None
    reason: str | None = None
    model_config = {"extra": "allow"}


class ErrorResponse(BaseModel):
    """Standard API error."""

    detail: str
    code: str | None = None
    context: dict[str, Any] | None = None
