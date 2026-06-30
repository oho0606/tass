"""Backtest Engine v1.0 — validates Rules with historical simulation (TASS-009)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import pandas as pd

from engine.backtest.config import BacktestEngineConfigData, load_backtest_config
from engine.backtest.registry import get_rule_evaluator
from engine.backtest.report import save_json_report, save_rule_markdown_report
from engine.backtest.rule_backtest import backtest_rule
from engine.backtest.types import BacktestRunResult, RuleBacktestResult
from engine.core.exceptions import BacktestException
from engine.core.logging import get_logger

logger = get_logger(__name__)


@dataclass
class BacktestEngineConfig:
    """Runtime configuration for ``BacktestEngine``."""

    config: BacktestEngineConfigData | None = None
    config_path: Path | None = None


@dataclass
class BacktestRunInput:
    """Input payload for a backtest run."""

    ohlcv_by_symbol: dict[str, pd.DataFrame]
    rule_ids: tuple[str, ...] | None = None
    data_source: str = "synthetic"


class BacktestEngine:
    """Orchestrates rule validation against historical OHLCV data.

    Backtest Engine does not modify Rules or Engines.
    It produces reproducible metrics for Rule adoption decisions.
    """

    def __init__(self, config: BacktestEngineConfig | None = None) -> None:
        """Initialize with optional YAML-backed configuration.

        Args:
            config: Engine config wrapper; loads default YAML when omitted.
        """
        self._config = _resolve_config(config)

    def run(self, run_input: BacktestRunInput) -> BacktestRunResult:
        """Execute backtest for configured rules across symbols.

        Args:
            run_input: OHLCV frames keyed by symbol and optional rule filter.

        Returns:
            Aggregated ``BacktestRunResult``.

        Raises:
            BacktestException: When no symbols or rules are available.
        """
        rule_ids = run_input.rule_ids or self._config.default_rules
        if not rule_ids:
            raise BacktestException("No rules configured for backtest.")
        if not run_input.ohlcv_by_symbol:
            raise BacktestException("No OHLCV data provided for backtest.")

        logger.info(
            "BacktestEngine.run rules={} symbols={}",
            rule_ids,
            list(run_input.ohlcv_by_symbol.keys()),
        )

        rule_results: list[RuleBacktestResult] = []
        for rule_id in rule_ids:
            try:
                evaluator = get_rule_evaluator(rule_id)
            except KeyError as exc:
                raise BacktestException(
                    f"Rule {rule_id} is not registered for backtest.",
                    context={"rule_id": rule_id},
                ) from exc
            for symbol, frame in run_input.ohlcv_by_symbol.items():
                result = backtest_rule(
                    rule_id=rule_id,
                    symbol=symbol,
                    df=frame,
                    evaluator=evaluator,
                    config=self._config,
                )
                rule_results.append(result)

        return BacktestRunResult(
            rule_results=rule_results,
            config_version=self._config.version,
            run_date=datetime.now().strftime("%Y-%m-%d"),
            data_source=run_input.data_source,
            reasons=["Backtest Engine v1.0 complete"],
        )

    def run_and_save(self, run_input: BacktestRunInput) -> tuple[BacktestRunResult, Path, tuple[Path, ...]]:
        """Run backtest and persist JSON + per-rule Markdown reports.

        Args:
            run_input: OHLCV frames and rule selection.

        Returns:
            Tuple of run result, JSON report path, and Markdown report paths.
        """
        result = self.run(run_input)
        output_dir = Path(self._config.output_dir)
        json_path = save_json_report(result, output_dir)
        markdown_paths: list[Path] = []
        for rule_result in result.rule_results:
            markdown_paths.append(save_rule_markdown_report(rule_result, output_dir))
        logger.info("Backtest reports saved to {}", output_dir)
        return result, json_path, tuple(markdown_paths)


def _resolve_config(config: BacktestEngineConfig | None) -> BacktestEngineConfigData:
    """Resolve configuration from wrapper or default path."""
    if config and config.config:
        return config.config
    if config and config.config_path:
        return load_backtest_config(config.config_path)
    return load_backtest_config()
