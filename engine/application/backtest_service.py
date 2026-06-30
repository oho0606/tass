"""Backtest application service — coordinates backtest I/O and Engine."""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path

import pandas as pd

from engine.application.market_data_loader import MarketDataLoadResult, load_universe_ohlcv
from engine.application.types import BacktestServiceResult
from engine.backtest import BacktestEngine, BacktestEngineConfig, BacktestRunInput
from engine.backtest.config import BacktestEngineConfigData, load_backtest_config
from engine.core.logging import get_logger

logger = get_logger(__name__)


class BacktestService:
    """Application service for Rule backtest runs.

    Delegates validation logic to ``BacktestEngine``; handles config and report I/O.
    """

    def __init__(
        self,
        config_path: Path | None = None,
        *,
        config: BacktestEngineConfigData | None = None,
    ) -> None:
        """Initialize with optional backtest YAML path or pre-loaded config.

        Args:
            config_path: Path to ``backtest_v1.yaml``.
            config: Pre-loaded config; takes precedence over path when both set.
        """
        self._config_path = config_path or Path("config/backtest_v1.yaml")
        self._config = config or load_backtest_config(self._config_path)
        self._engine = BacktestEngine(BacktestEngineConfig(config=self._config))

    @property
    def config(self) -> BacktestEngineConfigData:
        """Current backtest configuration."""
        return self._config

    def run_rule_backtest(
        self,
        ohlcv_by_symbol: dict[str, pd.DataFrame],
        *,
        rule_ids: tuple[str, ...] | None = None,
        data_source: str = "application",
        output_dir: Path | None = None,
    ) -> BacktestServiceResult:
        """Execute backtest and persist reports.

        Args:
            ohlcv_by_symbol: Symbol-keyed OHLCV frames.
            rule_ids: Rules to test; defaults to config ``default_rules``.
            data_source: Label recorded in run metadata.
            output_dir: Optional report directory override.

        Returns:
            ``BacktestServiceResult`` with paths to written reports.
        """
        cfg = self._config
        if output_dir is not None:
            cfg = replace(cfg, output_dir=str(output_dir))
            self._engine = BacktestEngine(BacktestEngineConfig(config=cfg))

        run_input = BacktestRunInput(
            ohlcv_by_symbol=ohlcv_by_symbol,
            rule_ids=rule_ids,
            data_source=data_source,
        )

        logger.info(
            "BacktestService.run_rule_backtest symbols={} rules={}",
            list(ohlcv_by_symbol.keys()),
            rule_ids or cfg.default_rules,
        )

        run_result, json_path, markdown_paths = self._engine.run_and_save(run_input)

        return BacktestServiceResult(
            run_result=run_result,
            report_path=json_path,
            markdown_paths=markdown_paths,
        )

    def load_market_data(
        self,
        universe_path: Path,
        *,
        lookback_days: int | None = None,
        use_cache: bool = True,
        fetch_missing: bool = True,
        cache_dir: Path | None = None,
    ) -> MarketDataLoadResult:
        """Load OHLCV for a KOSPI/KOSDAQ universe from cache or Yahoo."""
        data_cfg = self._config.data
        return load_universe_ohlcv(
            universe_path,
            lookback_days=lookback_days or data_cfg.lookback_days,
            use_cache=use_cache,
            fetch_missing=fetch_missing,
            min_bars=self._config.evaluation.min_bars,
            cache_dir=cache_dir or Path(data_cfg.cache_dir),
            adapter=data_cfg.adapter,
            compute_indicators=data_cfg.compute_indicators,
        )

    def run_universe_backtest(
        self,
        universe_path: Path,
        *,
        rule_ids: tuple[str, ...] | None = None,
        use_cache: bool = True,
        fetch_missing: bool = True,
        lookback_days: int | None = None,
        cache_dir: Path | None = None,
        output_dir: Path | None = None,
    ) -> BacktestServiceResult:
        """Load cached/live KRX OHLCV and run rule backtests."""
        market_data = self.load_market_data(
            universe_path,
            lookback_days=lookback_days,
            use_cache=use_cache,
            fetch_missing=fetch_missing,
            cache_dir=cache_dir,
        )
        if not market_data.ohlcv_by_symbol:
            raise ValueError(
                f"No OHLCV loaded for universe {universe_path}. "
                f"Skipped: {market_data.skipped_symbols}"
            )

        data_source = f"krx:{market_data.data_source}"
        return self.run_rule_backtest(
            market_data.ohlcv_by_symbol,
            rule_ids=rule_ids,
            data_source=data_source,
            output_dir=output_dir,
        )
