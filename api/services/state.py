"""API state: picks cache backed by Redis → PostgreSQL → file → engine."""

from __future__ import annotations

import json
import math
import threading
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Callable

from engine.application.recommendation_service import ProgressCallback, RecommendationService
from engine.application.serializers import pick_to_dict
from engine.application.settings import load_pipeline_settings
from engine.core.logging import get_logger
from engine.core.types import PickResult
from engine.data.engine import DataEngine
from engine.gate.market_context import load_market_context
from engine.recommendation.top20 import rank_top20

logger = get_logger(__name__)

DOMAIN_LABELS: dict[str, str] = {
    "trend": "Trend",
    "moving_average": "MA",
    "volume": "Volume",
    "momentum": "Momentum",
    "volatility": "Volatility",
    "support_resistance": "S/R",
    "pattern": "Pattern",
    "oscillator": "Oscillator",
}


@dataclass
class PicksCache:
    """Cached daily picks and full ranking."""

    date: str
    generated_at: str
    mvp_mode: bool
    universe_size: int
    candidates_evaluated: int
    picks: list[PickResult]
    gate_blocked: list[PickResult] = field(default_factory=list)
    all_ranked: list[PickResult] = field(default_factory=list)
    market_context: dict[str, Any] = field(default_factory=dict)


class TassApiState:
    """Thread-safe API state.

    Load priority: Redis → PostgreSQL → latest JSON file → live engine run.
    On fresh generation, persists to PostgreSQL + Redis.
    """

    def __init__(
        self,
        *,
        universe_path: Path | None = None,
        settings_path: Path | None = None,
        output_dir: Path | None = None,
    ) -> None:
        self._universe_path = universe_path or Path("config/universe_sample.csv")
        self._settings_path = settings_path or Path("config/settings.yaml")
        self._output_dir = output_dir or Path("output")
        self._lock = threading.Lock()
        self._cache: PicksCache | None = None
        self._service = RecommendationService(self._settings_path)
        self._settings = load_pipeline_settings(self._settings_path)

    @property
    def settings(self):
        return self._settings

    @property
    def is_cached(self) -> bool:
        return self._cache is not None

    def ensure_picks(
        self,
        *,
        refresh: bool = False,
        progress_callback: ProgressCallback | None = None,
    ) -> PicksCache:
        """Load or generate daily picks.

        Load order (when not refreshing):
          1. In-memory cache (instant)
          2. Redis cache (ms)
          3. PostgreSQL (sub-second)
          4. Latest JSON output file
          5. Live engine run → persist to PostgreSQL + Redis

        Args:
            refresh: If True, skip all caches and re-run the engine.
            progress_callback: ``(phase, percent, message)`` called during engine run.
        """
        with self._lock:
            if self._cache is not None and not refresh:
                return self._cache

            if not refresh:
                loaded = self._try_load_from_redis()
                if loaded is not None:
                    self._cache = loaded
                    return self._cache

            if not refresh:
                loaded = self._try_load_from_db()
                if loaded is not None:
                    self._cache = loaded
                    self._warm_redis(loaded)
                    return self._cache

            if not refresh:
                loaded = self._try_load_latest_json()
                if loaded is not None:
                    self._cache = loaded
                    return self._cache

            self._cache = self._generate_picks(progress_callback=progress_callback)
            self._persist(self._cache)
            return self._cache

    def get_pick(self, symbol: str) -> PickResult | None:
        cache = self.ensure_picks()
        normalized = symbol.strip()
        for pick in cache.all_ranked or cache.picks:
            if pick.symbol == normalized:
                return pick
        return None

    def market_status(self) -> dict[str, Any]:
        cache = self.ensure_picks()
        ctx = cache.market_context or {}
        kospi = str(ctx.get("kospi_trend", "UP"))
        kosdaq = str(ctx.get("kosdaq_trend", "UP"))
        market = str(ctx.get("market_trend", "UP"))
        regime = "Bull" if market == "UP" else "Bear" if market in ("DOWN", "CRASH") else "Neutral"
        return {
            "timestamp": datetime.now().isoformat(),
            "kospi_trend": kospi,
            "kosdaq_trend": kosdaq,
            "market_trend": market,
            "regime": regime,
            "picks_date": cache.date,
            "picks_count": len(cache.picks),
        }

    # ── Redis ────────────────────────────────────────────────────────────────

    def _try_load_from_redis(self) -> PicksCache | None:
        try:
            from api.cache.picks_cache import get_cached_picks

            payload = get_cached_picks()
            if payload is None:
                return None
            logger.info("Picks loaded from Redis (date={})", payload.get("pick_date"))
            return self._cache_from_payload(payload)
        except Exception as exc:
            logger.warning("Redis load failed: {}", exc)
            return None

    def _warm_redis(self, cache: PicksCache) -> None:
        try:
            from api.cache.picks_cache import cache_picks

            picks_dicts = [pick_to_dict(p) for p in cache.picks]
            blocked_dicts = [pick_to_dict(p) for p in cache.gate_blocked]
            cache_picks(
                pick_date=cache.date,
                picks=picks_dicts,
                gate_blocked=blocked_dicts,
                metadata={
                    "generated_at": cache.generated_at,
                    "mvp_mode": cache.mvp_mode,
                    "universe_size": cache.universe_size,
                    "candidates_evaluated": cache.candidates_evaluated,
                },
            )
        except Exception as exc:
            logger.warning("Redis warm failed: {}", exc)

    # ── PostgreSQL ───────────────────────────────────────────────────────────

    def _try_load_from_db(self) -> PicksCache | None:
        try:
            from api.db.repositories import get_picks_repo
            from api.db.session import get_session, is_db_available

            if not is_db_available():
                return None
            repo = get_picks_repo()
            with get_session() as session:
                result = repo.load_latest_picks(session)
                if result is None:
                    return None
                pick_date, picks_raw, blocked_raw = result
                logger.info("Picks loaded from PostgreSQL (date={})", pick_date)
                return self._cache_from_raw(
                    date_str=pick_date.isoformat(),
                    picks_raw=picks_raw,
                    blocked_raw=blocked_raw,
                )
        except Exception as exc:
            logger.warning("DB load failed: {}", exc)
            return None

    # ── File fallback ────────────────────────────────────────────────────────

    def _try_load_latest_json(self) -> PicksCache | None:
        if not self._output_dir.exists():
            return None
        files = sorted(self._output_dir.glob("picks_*.json"), reverse=True)
        if not files:
            return None
        try:
            payload = json.loads(files[0].read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return None
        picks_raw = payload.get("picks") or []
        if not picks_raw:
            return None
        return self._cache_from_payload(payload)

    # ── Engine run ───────────────────────────────────────────────────────────

    def _generate_picks(
        self,
        progress_callback: ProgressCallback | None = None,
    ) -> PicksCache:
        result = self._service.generate_daily_picks(
            self._universe_path,
            use_cache=True,
            progress_callback=progress_callback,
        )
        all_ranked = self._rank_all_candidates()
        market_ctx = self._fetch_market_context()
        return PicksCache(
            date=result.date,
            generated_at=result.generated_at,
            mvp_mode=result.mvp_mode,
            universe_size=result.universe_size,
            candidates_evaluated=result.candidates_evaluated,
            picks=list(result.picks),
            gate_blocked=list(result.gate_blocked),
            all_ranked=all_ranked or list(result.picks),
            market_context=market_ctx,
        )

    # ── Persistence ──────────────────────────────────────────────────────────

    def _persist(self, cache: PicksCache) -> None:
        """Save freshly generated picks to PostgreSQL + Redis (best-effort)."""
        picks_dicts = [pick_to_dict(p) for p in cache.picks]
        blocked_dicts = [pick_to_dict(p) for p in cache.gate_blocked]

        # PostgreSQL
        try:
            from api.db.repositories import get_picks_repo
            from api.db.session import get_session, is_db_available

            if is_db_available():
                repo = get_picks_repo()
                pick_date = date.fromisoformat(cache.date)
                with get_session() as session:
                    repo.save_picks(session, pick_date, picks_dicts, blocked_dicts)
        except Exception as exc:
            logger.warning("DB persist failed (non-fatal): {}", exc)

        # Redis
        try:
            from api.cache.picks_cache import cache_picks

            cache_picks(
                pick_date=cache.date,
                picks=picks_dicts,
                gate_blocked=blocked_dicts,
                metadata={
                    "generated_at": cache.generated_at,
                    "mvp_mode": cache.mvp_mode,
                    "universe_size": cache.universe_size,
                    "candidates_evaluated": cache.candidates_evaluated,
                },
            )
        except Exception as exc:
            logger.warning("Redis persist failed (non-fatal): {}", exc)

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _cache_from_payload(self, payload: dict[str, Any]) -> PicksCache | None:
        picks_raw = payload.get("picks") or []
        if not picks_raw:
            return None
        blocked_raw = payload.get("gate_blocked") or []
        date_str = str(payload.get("pick_date") or payload.get("date", ""))
        market_ctx = self._fetch_market_context()
        picks = [self._pick_from_dict(item) for item in picks_raw]
        blocked = [self._pick_from_dict(item) for item in blocked_raw]
        return PicksCache(
            date=date_str,
            generated_at=str(payload.get("generated_at", "")),
            mvp_mode=bool(payload.get("mvp_mode", True)),
            universe_size=int(payload.get("universe_size", 0)),
            candidates_evaluated=int(payload.get("candidates_evaluated", 0)),
            picks=picks,
            gate_blocked=blocked,
            all_ranked=picks,
            market_context=market_ctx,
        )

    def _cache_from_raw(
        self,
        date_str: str,
        picks_raw: list[dict],
        blocked_raw: list[dict],
    ) -> PicksCache:
        market_ctx = self._fetch_market_context()
        picks = [self._pick_from_dict(r) for r in picks_raw]
        blocked = [self._pick_from_dict(r) for r in blocked_raw]
        return PicksCache(
            date=date_str,
            generated_at=str(picks_raw[0].get("generated_at", "") if picks_raw else ""),
            mvp_mode=bool(picks_raw[0].get("mvp_mode", True) if picks_raw else True),
            universe_size=int(picks_raw[0].get("universe_size", 0) if picks_raw else 0),
            candidates_evaluated=0,
            picks=picks,
            gate_blocked=blocked,
            all_ranked=picks,
            market_context=market_ctx,
        )

    def _rank_all_candidates(self) -> list[PickResult]:
        """Evaluate full universe and rank all candidates for /ranking."""
        if not self._universe_path.exists():
            return []
        from engine.data.universe import load_universe

        universe = load_universe(self._universe_path)
        data_engine = DataEngine(self._settings.to_data_engine_config())
        gate_cfg = self._settings.to_gate_config()
        market_context = self._fetch_market_context()
        candidates = []
        evaluate = self._service._evaluate_entry  # noqa: SLF001 — application bridge
        for entry in universe:
            candidate = evaluate(
                entry=entry,
                data_engine=data_engine,
                gate_cfg=gate_cfg,
                use_cache=True,
                ohlcv_overrides=None,
                market_context=market_context,
            )
            if candidate is not None:
                candidates.append(candidate)
        if not candidates:
            return []
        return rank_top20(candidates, top_n=len(candidates), eligible_only=False).picks

    def _fetch_market_context(self) -> dict[str, Any]:
        try:
            data_engine = DataEngine(self._settings.to_data_engine_config())
            return load_market_context(data_engine, use_cache=True)
        except Exception:
            return {"market_trend": "UP", "kospi_trend": "UP", "kosdaq_trend": "UP"}

    @staticmethod
    def _pick_from_dict(data: dict[str, Any]) -> PickResult:
        return PickResult(
            rank=int(data.get("rank", 0)),
            symbol=str(data.get("symbol", "")),
            name=str(data.get("name", "")),
            total_score=float(data.get("total_score", 0)),
            max_score=float(data.get("max_score", 1000)),
            domains=dict(data.get("domains") or {}),
            confidence=data.get("confidence"),
            risk=data.get("risk"),
            reasons=list(data.get("reasons") or []),
            gate=data.get("gate", "PASS"),  # type: ignore[arg-type]
            grade=data.get("grade"),
            probability=data.get("probability"),
            probability_grade=data.get("probability_grade"),
            probability_level=data.get("probability_level"),
            risk_grade=data.get("risk_grade"),
            risk_grade_stars=data.get("risk_grade_stars"),
            risk_level=data.get("risk_level"),
            risk_decision=data.get("risk_decision"),
            risk_breakdown=data.get("risk_breakdown"),
            confidence_grade=data.get("confidence_grade"),
            confidence_level=data.get("confidence_level"),
            confidence_stars=data.get("confidence_stars"),
            recommendation=data.get("recommendation"),
            recommendation_grade=data.get("recommendation_grade"),
            recommendation_reason=data.get("recommendation_reason"),
            passed_conditions=data.get("passed_conditions"),
            failed_conditions=data.get("failed_conditions"),
            gate_report=data.get("gate_report"),
            composite_breakdown=data.get("composite_breakdown"),
        )


# ── Convenience functions (unchanged public API) ──────────────────────────────


def pick_detail_from_result(pick: PickResult):
    """Convert PickResult to PickDetail schema via serializer."""
    from api.schemas.picks import PickDetail

    data = pick_to_dict(pick)
    return PickDetail.model_validate(data)


def pick_summary_from_result(pick: PickResult):
    from api.schemas.picks import PickSummary

    return PickSummary(
        rank=pick.rank,
        symbol=pick.symbol,
        name=pick.name,
        total_score=pick.total_score,
        max_score=pick.max_score,
        grade=pick.grade,
        confidence=pick.confidence,
        confidence_stars=pick.confidence_stars,
        risk=pick.risk,
        risk_level=pick.risk_level,
        probability=pick.probability,
        recommendation=pick.recommendation,
        recommendation_grade=pick.recommendation_grade,
        gate=pick.gate,
    )


def paginate(items: list, page: int, page_size: int) -> tuple[list, int, int]:
    total = len(items)
    total_pages = max(1, math.ceil(total / page_size)) if total else 0
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end], total, total_pages


def domain_views_from_pick(pick: PickResult) -> tuple[list, dict[str, float]]:
    from api.schemas.common import DomainScoreView

    views: list[DomainScoreView] = []
    radar: dict[str, float] = {}
    for key, value in (pick.domains or {}).items():
        if not value or not isinstance(value, dict):
            continue
        score = float(value.get("score", 0))
        max_score = float(value.get("max", value.get("max_score", 100)))
        label = DOMAIN_LABELS.get(key, key.replace("_", " ").title())
        views.append(
            DomainScoreView(
                key=key,
                label=label,
                score=score,
                max_score=max_score,
                grade=value.get("grade"),
                state=value.get("state"),
                status=str(value.get("status", "implemented")),
            )
        )
        radar[label] = round((score / max_score * 100) if max_score else 0, 1)
    return views, radar
