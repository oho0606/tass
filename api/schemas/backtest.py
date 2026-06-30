"""Pydantic models for backtest summary endpoint."""

from __future__ import annotations

from pydantic import BaseModel, Field


class BacktestRuleSummary(BaseModel):
    """Aggregated metrics for one rule backtest."""

    rule_id: str
    symbol: str
    verdict: str
    total_return_pct: float
    win_rate: float
    max_drawdown_pct: float
    sharpe_ratio: float
    trade_count: int
    sample_days: int


class BacktestSummaryResponse(BaseModel):
    """Overall backtest summary for UI table."""

    run_date: str | None = None
    config_version: str | None = None
    data_source: str | None = None
    rule_count: int = 0
    adopt_count: int = 0
    reject_count: int = 0
    rules: list[BacktestRuleSummary] = Field(default_factory=list)
    available: bool = False
    message: str | None = None
