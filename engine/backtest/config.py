"""Configuration loader for Backtest Engine v1.0."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass(frozen=True)
class TradingConfig:
    """Trade simulation parameters."""

    commission_rate: float = 0.00015
    slippage_rate: float = 0.001
    initial_capital: float = 100_000_000.0
    entry_mode: str = "next_open"
    hold_days: int = 20
    stop_loss_pct: float = 0.05
    take_profit_pct: float = 0.15


@dataclass(frozen=True)
class EvaluationConfig:
    """Rule adoption thresholds."""

    min_bars: int = 60
    min_trades: int = 5
    in_sample_ratio: float = 0.7
    min_win_rate: float = 0.40
    max_drawdown_pct: float = 0.30


@dataclass(frozen=True)
class BacktestDataConfig:
    """Real-data backtest data settings."""

    lookback_days: int = 3650
    cache_dir: str = "data/cache"
    adapter: str = "yahoo"
    default_universe: str = "config/universe_krx_backtest.csv"
    compute_indicators: bool = False


@dataclass(frozen=True)
class BacktestEngineConfigData:
    """Frozen backtest configuration."""

    version: str = "1.0"
    status: str = "frozen"
    trading: TradingConfig = field(default_factory=TradingConfig)
    evaluation: EvaluationConfig = field(default_factory=EvaluationConfig)
    data: BacktestDataConfig = field(default_factory=BacktestDataConfig)
    default_rules: tuple[str, ...] = ("TR0001", "TR0002", "TR0003", "TR0004")
    output_dir: str = "backtest/reports"


def load_backtest_config(path: Path | None = None) -> BacktestEngineConfigData:
    """Load backtest configuration from YAML.

    Args:
        path: Config file path; defaults to ``config/backtest_v1.yaml``.

    Returns:
        Parsed ``BacktestEngineConfigData``.

    Example:
        >>> cfg = load_backtest_config()
        >>> cfg.trading.hold_days
        20
    """
    if path is None:
        path = Path("config/backtest_v1.yaml")
    if not path.exists():
        return BacktestEngineConfigData()

    with path.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    trading_raw = raw.get("trading") or {}
    evaluation_raw = raw.get("evaluation") or {}
    trading = TradingConfig(
        commission_rate=float(trading_raw.get("commission_rate", 0.00015)),
        slippage_rate=float(trading_raw.get("slippage_rate", 0.001)),
        initial_capital=float(trading_raw.get("initial_capital", 100_000_000)),
        entry_mode=str(trading_raw.get("entry_mode", "next_open")),
        hold_days=int(trading_raw.get("hold_days", 20)),
        stop_loss_pct=float(trading_raw.get("stop_loss_pct", 0.05)),
        take_profit_pct=float(trading_raw.get("take_profit_pct", 0.15)),
    )
    evaluation = EvaluationConfig(
        min_bars=int(evaluation_raw.get("min_bars", 60)),
        min_trades=int(evaluation_raw.get("min_trades", 5)),
        in_sample_ratio=float(evaluation_raw.get("in_sample_ratio", 0.7)),
        min_win_rate=float(evaluation_raw.get("min_win_rate", 0.40)),
        max_drawdown_pct=float(evaluation_raw.get("max_drawdown_pct", 0.30)),
    )
    data_raw = raw.get("data") or {}
    data = BacktestDataConfig(
        lookback_days=int(data_raw.get("lookback_days", 3650)),
        cache_dir=str(data_raw.get("cache_dir", "data/cache")),
        adapter=str(data_raw.get("adapter", "yahoo")),
        default_universe=str(
            data_raw.get("default_universe", "config/universe_krx_backtest.csv")
        ),
        compute_indicators=bool(data_raw.get("compute_indicators", False)),
    )
    default_rules = tuple(str(rule_id) for rule_id in raw.get("default_rules", [])) or (
        "TR0001",
        "TR0002",
        "TR0003",
        "TR0004",
    )

    return BacktestEngineConfigData(
        version=str(raw.get("version", "1.0")),
        status=str(raw.get("status", "frozen")),
        trading=trading,
        evaluation=evaluation,
        data=data,
        default_rules=default_rules,
        output_dir=str(raw.get("output_dir", "backtest/reports")),
    )
