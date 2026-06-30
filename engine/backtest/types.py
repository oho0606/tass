"""Backtest domain types (TASS-009, TASS-030)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Literal

BacktestVerdict = Literal["ADOPT", "REJECT", "REVISE", "INSUFFICIENT_DATA"]


@dataclass(frozen=True)
class TradeRecord:
    """Single simulated trade outcome."""

    entry_date: date
    exit_date: date
    entry_price: float
    exit_price: float
    return_pct: float
    pnl: float
    exit_reason: str


@dataclass(frozen=True)
class BacktestMetrics:
    """Performance metrics required by TASS-009 §8."""

    total_return_pct: float
    cagr_pct: float
    win_rate: float
    avg_win_pct: float
    avg_loss_pct: float
    reward_risk_ratio: float
    profit_factor: float
    max_drawdown_pct: float
    sharpe_ratio: float
    sortino_ratio: float
    trade_count: int
    sample_days: int


@dataclass
class SplitMetrics:
    """In-sample / out-of-sample metric comparison."""

    in_sample: BacktestMetrics
    out_of_sample: BacktestMetrics


@dataclass
class RuleBacktestResult:
    """Backtest result for a single Rule."""

    rule_id: str
    symbol: str
    metrics: BacktestMetrics
    split_metrics: SplitMetrics | None
    trades: list[TradeRecord]
    verdict: BacktestVerdict
    reasons: list[str] = field(default_factory=list)
    version: str = "1.0"


@dataclass
class BacktestRunResult:
    """Aggregated backtest run output."""

    rule_results: list[RuleBacktestResult]
    config_version: str
    run_date: str
    data_source: str
    reasons: list[str] = field(default_factory=list)
