#!/usr/bin/env python3
"""Compare pipeline metrics under current vs bull market regime (Phase 6).

Uses cached real OHLCV with synthetic market-context overrides to validate
that gate pass pools expand when KOSDAQ exits CRASH (listing-aware gate).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.application.recommendation_service import RecommendationService
from engine.data.engine import DataEngine
from engine.data.universe import load_universe
from engine.gate.market_context import load_market_context
from engine.recommendation.config import load_recommendation_config
from engine.recommendation.recommendation_engine import (
    RecommendationEngineConfigWrapper,
    RecommendationEngineInput,
    compute_recommendations,
)
from engine.recommendation.top20 import is_gate_eligible, rank_top20

REGIME_SCENARIOS = {
    "current": None,
    "bull": {"kospi_trend": "UP", "kosdaq_trend": "UP", "market_trend": "UP"},
}


def _gate_fail_counts(candidates) -> dict[str, int]:
    counts: dict[str, int] = {}
    for candidate in candidates:
        if is_gate_eligible(candidate.gate_status):
            continue
        for report in candidate.pipeline_gate_report or []:
            if report.get("source") == "pipeline" and report.get("status") == "FAIL":
                key = str(report.get("gate_key", "unknown"))
                counts[key] = counts.get(key, 0) + 1
                break
    return counts


def evaluate_regime(
    universe_path: Path,
    *,
    regime: str,
    top_n: int,
    use_cache: bool,
) -> dict:
    if regime not in REGIME_SCENARIOS:
        raise ValueError(f"Unknown regime: {regime}")

    service = RecommendationService()
    universe = load_universe(universe_path)
    data_engine = DataEngine(service.settings.to_data_engine_config())
    gate_cfg = service.settings.to_gate_config()

    if REGIME_SCENARIOS[regime] is None:
        market_context = load_market_context(data_engine, use_cache=use_cache)
    else:
        market_context = REGIME_SCENARIOS[regime]

    candidates = []
    for entry in universe:
        candidate = service._evaluate_entry(
            entry=entry,
            data_engine=data_engine,
            gate_cfg=gate_cfg,
            use_cache=use_cache,
            ohlcv_overrides=None,
            market_context=market_context,
        )
        if candidate is not None:
            candidates.append(candidate)

    gate_eligible = [c for c in candidates if is_gate_eligible(c.gate_status)]
    ranked = rank_top20(candidates, top_n=top_n)

    rec_inputs: list[RecommendationEngineInput] = []
    for candidate in gate_eligible:
        if candidate.risk is None:
            continue
        rec_inputs.append(
            RecommendationEngineInput(
                symbol=candidate.symbol,
                name=candidate.name,
                master=candidate.master,
                probability=candidate.probability,
                confidence=candidate.confidence,
                risk=candidate.risk,
                trend=candidate.trend,
                data_quality_pass=candidate.data_quality_pass,
                volume=candidate.volume,
                gate_status=candidate.gate_status,
                pipeline_gate_report=candidate.pipeline_gate_report,
            )
        )

    rec_cfg = RecommendationEngineConfigWrapper(config=load_recommendation_config())
    rec_results = compute_recommendations(rec_inputs, top_n=top_n, config=rec_cfg)
    rec_pool = sum(1 for result in rec_results if result.is_candidate)

    return {
        "regime": regime,
        "market_context": market_context,
        "universe_size": len(universe),
        "candidates_evaluated": len(candidates),
        "gate_eligible": len(gate_eligible),
        "gate_fail_by_key": _gate_fail_counts(candidates),
        "picks": len(ranked.picks),
        "gate_blocked": len(ranked.gate_blocked),
        "recommendation_pool": rec_pool,
        "recommendation_picks": sum(1 for r in rec_results if r.recommendation_rank),
    }


def validate_regimes(
    universe_path: Path,
    *,
    top_n: int = 20,
    use_cache: bool = True,
    min_bull_gate_eligible: int = 18,
) -> dict:
    current = evaluate_regime(universe_path, regime="current", top_n=top_n, use_cache=use_cache)
    bull = evaluate_regime(universe_path, regime="bull", top_n=top_n, use_cache=use_cache)

    checks = [
        {
            "name": "current_regime_has_picks",
            "passed": current["picks"] >= 1,
            "detail": f"{current['picks']} picks, gate_eligible={current['gate_eligible']}",
        },
        {
            "name": "bull_expands_gate_pool",
            "passed": bull["gate_eligible"] >= current["gate_eligible"],
            "detail": (
                f"bull gate_eligible={bull['gate_eligible']} "
                f"vs current={current['gate_eligible']}"
            ),
        },
        {
            "name": "bull_regime_baseline",
            "passed": bull["gate_eligible"] >= min_bull_gate_eligible,
            "detail": f"bull gate_eligible={bull['gate_eligible']} (min {min_bull_gate_eligible})",
        },
        {
            "name": "recommendation_not_bottleneck_current",
            "passed": current["recommendation_pool"] >= current["picks"],
            "detail": (
                f"rec_pool={current['recommendation_pool']} picks={current['picks']} "
                f"(gate is primary filter)"
            ),
        },
    ]

    passed = all(check["passed"] for check in checks)
    return {
        "passed": passed,
        "universe": str(universe_path),
        "top_n": top_n,
        "scenarios": {"current": current, "bull": bull},
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate current vs bull regime baselines")
    parser.add_argument("--universe", type=Path, default=Path("config/universe_krx_mvp.csv"))
    parser.add_argument("--top-n", type=int, default=20)
    parser.add_argument("--min-bull-gate-eligible", type=int, default=18)
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument("--output", type=Path, default=Path("output/regime_validation.json"))
    args = parser.parse_args()

    report = validate_regimes(
        args.universe,
        top_n=args.top_n,
        use_cache=not args.no_cache,
        min_bull_gate_eligible=args.min_bull_gate_eligible,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
