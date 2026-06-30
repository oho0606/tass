"""Recommendation application service — coordinates I/O and Engine pipeline."""

from __future__ import annotations

from dataclasses import replace
from datetime import date, datetime
from pathlib import Path
from typing import Callable

import pandas as pd

from engine.application.serializers import save_daily_picks_json
from engine.application.settings import PipelineSettings, load_pipeline_settings
from engine.application.types import DailyPicksResult
from engine.core.exceptions import DataException, RecommendationException
from engine.core.logging import get_logger
from engine.data.engine import DataEngine
from engine.data.universe import UniverseEntry, load_universe
from engine.domains.bundle import evaluate_domain_bundle
from engine.domains.moving_average_engine import evaluate_moving_average_engine
from engine.domains.trend_engine import evaluate_trend_engine
from engine.domains.volume_engine import evaluate_volume_engine
from engine.gate.evaluate import evaluate_symbol_gates
from engine.gate.market_context import load_market_context
from engine.indicators.registry import compute_all
from engine.recommendation.top20 import build_candidate, rank_top20
from engine.scoring import compute_master_score

logger = get_logger(__name__)

# phase, percent(0-100), message
ProgressCallback = Callable[[str, int, str], None]


def _noop_callback(phase: str, pct: int, msg: str) -> None:  # noqa: ARG001
    pass


class RecommendationService:
    """Application service for Today's Picks generation.

    Business logic remains in Engine layer; this service loads data,
    invokes engines, ranks candidates, and optionally persists output.
    """

    def __init__(self, settings_path: Path | None = None) -> None:
        """Initialize with optional settings YAML path.

        Args:
            settings_path: Path to ``settings.yaml``; defaults to ``config/settings.yaml``.
        """
        self._settings_path = settings_path or Path("config/settings.yaml")
        self._settings = load_pipeline_settings(self._settings_path)

    @property
    def settings(self) -> PipelineSettings:
        """Current pipeline settings."""
        return self._settings

    def generate_daily_picks(
        self,
        universe_path: Path,
        *,
        use_cache: bool = True,
        ohlcv_overrides: dict[str, pd.DataFrame] | None = None,
        market_context: dict | None = None,
        progress_callback: ProgressCallback | None = None,
    ) -> DailyPicksResult:
        """Run full recommendation pipeline for a universe.

        Args:
            universe_path: CSV listing symbols to analyze.
            use_cache: Whether to use OHLCV cache when fetching live data.
            ohlcv_overrides: Optional symbol→DataFrame map for offline/testing.
            progress_callback: Optional ``(phase, percent, message)`` callable called
                at each pipeline stage to report real-time progress.

        Returns:
            ``DailyPicksResult`` with ranked picks.

        Raises:
            DataException: When universe file cannot be loaded.
            RecommendationException: When no candidates can be evaluated.
        """
        cb = progress_callback or _noop_callback

        if not universe_path.exists():
            raise DataException(
                f"Universe file not found: {universe_path}",
                context={"path": str(universe_path)},
            )

        universe = load_universe(universe_path)
        if not universe:
            raise DataException(
                "Universe file is empty.",
                context={"path": str(universe_path)},
            )

        total = len(universe)
        logger.info(
            "RecommendationService.generate_daily_picks universe={} size={}",
            universe_path,
            total,
        )

        cb("universe", 5, f"유니버스 로드 완료 ({total}개 종목)")

        data_engine = DataEngine(self._settings.to_data_engine_config())
        gate_cfg = self._settings.to_gate_config()

        cb("market_context", 8, "시장 컨텍스트 분석 중")
        resolved_market_context = market_context or load_market_context(
            data_engine,
            use_cache=use_cache,
        )
        cb("market_context", 10, "시장 컨텍스트 분석 완료")

        candidates = []

        # Per-symbol progress: 10% → 75%
        _pct_range = 65
        for i, entry in enumerate(universe):
            symbol_pct = 10 + round(_pct_range * (i + 1) / total)
            cb(
                "evaluating",
                symbol_pct,
                f"{entry.symbol} 분석 중 ({i + 1}/{total})",
            )
            candidate = self._evaluate_entry(
                entry=entry,
                data_engine=data_engine,
                gate_cfg=gate_cfg,
                use_cache=use_cache,
                ohlcv_overrides=ohlcv_overrides,
                market_context=resolved_market_context,
            )
            if candidate is not None:
                candidates.append(candidate)

        if not candidates:
            raise RecommendationException(
                "No candidates evaluated — check universe and data availability.",
                context={"universe_size": total},
            )

        cb("ranking", 78, f"포트폴리오 랭킹 산정 중 ({len(candidates)}개 후보)")
        ranked = rank_top20(candidates, top_n=self._settings.top_n)
        cb("ranking", 82, "Top 20 확정")

        today = date.today().isoformat()

        return DailyPicksResult(
            date=today,
            generated_at=datetime.now().isoformat(),
            mvp_mode=self._settings.mvp_mode,
            universe_size=total,
            candidates_evaluated=len(candidates),
            picks=tuple(ranked.picks),
            gate_blocked=tuple(ranked.gate_blocked),
        )

    def save_daily_picks(
        self,
        result: DailyPicksResult,
        output_dir: Path | None = None,
    ) -> DailyPicksResult:
        """Persist picks JSON and return result with ``output_path`` set.

        Args:
            result: Generated daily picks.
            output_dir: Override output directory from settings.

        Returns:
            Updated ``DailyPicksResult`` including output path.
        """
        target_dir = output_dir or self._settings.output_dir
        path = save_daily_picks_json(result, target_dir)
        logger.info("Daily picks saved path={}", path)
        return replace(result, output_path=path)

    def run_daily_picks(
        self,
        universe_path: Path,
        *,
        use_cache: bool = True,
        output_dir: Path | None = None,
        ohlcv_overrides: dict[str, pd.DataFrame] | None = None,
        market_context: dict | None = None,
        progress_callback: ProgressCallback | None = None,
    ) -> DailyPicksResult:
        """Generate and save Today's Picks in one call.

        Args:
            universe_path: CSV listing symbols to analyze.
            use_cache: Whether to use OHLCV cache.
            output_dir: Optional output directory override.
            ohlcv_overrides: Optional offline OHLCV map keyed by symbol.
            progress_callback: Optional ``(phase, percent, message)`` callable.

        Returns:
            ``DailyPicksResult`` with output path populated.
        """
        result = self.generate_daily_picks(
            universe_path,
            use_cache=use_cache,
            ohlcv_overrides=ohlcv_overrides,
            market_context=market_context,
            progress_callback=progress_callback,
        )
        return self.save_daily_picks(result, output_dir=output_dir)

    def _evaluate_entry(
        self,
        *,
        entry: UniverseEntry,
        data_engine: DataEngine,
        gate_cfg,
        use_cache: bool,
        ohlcv_overrides: dict[str, pd.DataFrame] | None,
        market_context: dict | None = None,
    ):
        """Evaluate one universe entry through engine pipeline."""
        if ohlcv_overrides is not None and entry.symbol in ohlcv_overrides:
            df = ohlcv_overrides[entry.symbol].copy()
            from engine.data.validator import validate_ohlcv

            validation = validate_ohlcv(df, min_bars=self._settings.min_bars)
        else:
            yahoo_sym = data_engine.adapter.to_yahoo_symbol(entry.symbol, entry.market)
            df, validation = data_engine.get_ohlcv(yahoo_sym, use_cache=use_cache)
            if df.empty:
                logger.warning("Skipping {} — empty OHLCV", entry.symbol)
                return None

        if df.empty:
            logger.warning("Skipping {} — empty OHLCV override", entry.symbol)
            return None

        df = compute_all(df)
        if self._settings.mvp_mode:
            trend = evaluate_trend_engine(df)
            moving_average = evaluate_moving_average_engine(df)
            volume_result = evaluate_volume_engine(df)
            master = compute_master_score(
                trend=trend,
                moving_average=moving_average,
                volume=volume_result,
                mvp_mode=True,
            )
        else:
            bundle = evaluate_domain_bundle(df)
            trend = bundle.trend
            master = compute_master_score(bundle=bundle, mvp_mode=False)
        gate_eval = evaluate_symbol_gates(
            df=df,
            trend=trend,
            data_valid=validation.valid,
            gate_cfg=gate_cfg,
            master=master,
            market_context=market_context,
            listing_market=entry.market,
        )
        master = gate_eval.adjusted_master or master

        return build_candidate(
            entry,
            master,
            trend,
            gate_eval.gate_status,
            df=df,
            gate=gate_eval.legacy_gate,
            data_valid=validation.valid,
            data_quality=validation,
            pipeline_gate_report=gate_eval.gate_report,
        )
