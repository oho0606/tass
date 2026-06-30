"""Backtest summary router."""

from __future__ import annotations

from fastapi import APIRouter

from api.schemas.backtest import BacktestSummaryResponse
from api.services.backtest_data import load_backtest_summary

router = APIRouter(tags=["backtest"])


@router.get("/backtest/summary", response_model=BacktestSummaryResponse)
def backtest_summary() -> BacktestSummaryResponse:
    """Return aggregated backtest statistics from latest report."""
    return load_backtest_summary()
