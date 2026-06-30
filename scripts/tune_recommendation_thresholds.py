#!/usr/bin/env python3
"""Dry-run threshold sweep for Recommendation Engine v1.0 (Phase 6).

Evaluates cached universe OHLCV and searches gate thresholds that yield
10–30 recommendable candidates while keeping top_n stable picks.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import replace
from itertools import product
from pathlib import Path

from engine.application.recommendation_service import RecommendationService
from engine.gate.market_context import load_market_context
from engine.recommendation.config import GateThresholds, load_recommendation_config
from engine.recommendation.recommendation_engine import (
    RecommendationEngineConfigWrapper,
    RecommendationEngineInput,
    compute_recommendations,
)
from engine.recommendation.top20 import is_gate_eligible


def _collect_engine_inputs(
    universe_path: Path,
    *,
    settings_path: Path,
    use_cache: bool,
    market_context: dict | None = None,
    gate_eligible_only: bool = True,
) -> tuple[list[RecommendationEngineInput], dict]:
    service = RecommendationService(settings_path=settings_path)
    universe = __import__(
        "engine.data.universe", fromlist=["load_universe"]
    ).load_universe(universe_path)
    data_engine = __import__(
        "engine.data.engine", fromlist=["DataEngine"]
    ).DataEngine(service.settings.to_data_engine_config())
    gate_cfg = service.settings.to_gate_config()
    market_context = market_context or load_market_context(data_engine, use_cache=use_cache)

    inputs: list[RecommendationEngineInput] = []
    evaluated = 0
    gate_eligible_count = 0
    for entry in universe:
        candidate = service._evaluate_entry(
            entry=entry,
            data_engine=data_engine,
            gate_cfg=gate_cfg,
            use_cache=use_cache,
            ohlcv_overrides=None,
            market_context=market_context,
        )
        if candidate is None or candidate.risk is None:
            continue
        evaluated += 1
        if gate_eligible_only and not is_gate_eligible(candidate.gate_status):
            continue
        gate_eligible_count += 1
        prob = candidate.probability
        conf = candidate.confidence
        inputs.append(
            RecommendationEngineInput(
                symbol=candidate.symbol,
                name=candidate.name,
                master=candidate.master,
                probability=prob,
                confidence=conf,
                risk=candidate.risk,
                trend=candidate.trend,
                data_quality_pass=candidate.data_quality_pass,
                volume=candidate.volume,
                gate_status=candidate.gate_status,
                pipeline_gate_report=candidate.pipeline_gate_report,
            )
        )
    meta = {
        "evaluated": evaluated,
        "gate_eligible": gate_eligible_count,
        "market_context": market_context,
        "mvp_mode": service.settings.mvp_mode,
    }
    return inputs, meta


def _count_picks(
    inputs: list[RecommendationEngineInput],
    gates: GateThresholds,
    top_n: int,
    recommendation_config_path: Path,
) -> tuple[int, int]:
    base = load_recommendation_config(path=recommendation_config_path)
    cfg = replace(base, gates=gates)
    wrapper = RecommendationEngineConfigWrapper(config=cfg)
    results = compute_recommendations(inputs, top_n=top_n, config=wrapper)
    pool = sum(1 for r in results if r.is_candidate)
    picks = sum(1 for r in results if r.is_candidate and r.recommendation_rank is not None)
    return pool, picks


def sweep_thresholds(
    inputs: list[RecommendationEngineInput],
    *,
    mvp_mode: bool,
    recommendation_config_path: Path,
    top_n: int,
    target_min: int,
    target_max: int,
) -> list[dict]:
    base = load_recommendation_config(path=recommendation_config_path).gates
    available = len(inputs)
    target_picks = min(top_n, available)
    if mvp_mode:
        grid = {
            "master_score_min": [180, 200, 220, 250, 300, 350, 400],
            "probability_min": [12.0, 15.0, 18.0, 20.0, 25.0],
            "confidence_min": [50.0, 55.0, 60.0, 65.0],
            "risk_max": [55.0, 60.0, 65.0, 70.0, 75.0],
            "max_composite_failures": [2, 3, 4, 5, 6],
            "critical_conflict_min_pass": [10],
            "critical_conflict_min_fail": [10],
        }
    else:
        # Full-mode grid (1000-pt scale) with stricter master-score floors.
        grid = {
            "master_score_min": [520, 560, 600, 650, 700, 750, 800],
            "probability_min": [20.0, 25.0, 30.0, 35.0, 40.0],
            "confidence_min": [55.0, 60.0, 65.0, 70.0, 75.0],
            "risk_max": [45.0, 50.0, 55.0, 60.0, 65.0],
            "max_composite_failures": [0, 1, 2, 3],
            "critical_conflict_min_pass": [2, 4, 6],
            "critical_conflict_min_fail": [2, 4, 6],
        }

    matches: list[dict] = []
    for (
        master_min,
        prob_min,
        conf_min,
        risk_max,
        comp_fail,
        crit_pass,
        crit_fail,
    ) in product(
        grid["master_score_min"],
        grid["probability_min"],
        grid["confidence_min"],
        grid["risk_max"],
        grid["max_composite_failures"],
        grid["critical_conflict_min_pass"],
        grid["critical_conflict_min_fail"],
    ):
        gates = replace(
            base,
            master_score_min=float(master_min),
            probability_min=float(prob_min),
            confidence_min=float(conf_min),
            risk_max=float(risk_max),
            max_composite_failures=int(comp_fail),
            critical_conflict_min_pass=int(crit_pass),
            critical_conflict_min_fail=int(crit_fail),
        )
        pool, picks = _count_picks(inputs, gates, top_n, recommendation_config_path)
        if target_min <= pool <= target_max and picks >= max(1, min(target_min, target_picks)):
            score = abs(pool - target_picks) + abs(picks - target_picks)
            matches.append(
                {
                    "score": score,
                    "pool": pool,
                    "picks": picks,
                    "gates": {
                        "master_score_min": master_min,
                        "probability_min": prob_min,
                        "confidence_min": conf_min,
                        "risk_max": risk_max,
                        "max_composite_failures": comp_fail,
                        "critical_conflict_min_pass": crit_pass,
                        "critical_conflict_min_fail": crit_fail,
                    },
                }
            )

    matches.sort(key=lambda item: (item["score"], -item["pool"]))
    return matches


def main() -> int:
    parser = argparse.ArgumentParser(description="Tune recommendation_v1.yaml thresholds")
    parser.add_argument("--universe", type=Path, default=Path("config/universe_krx_mvp.csv"))
    parser.add_argument(
        "--settings",
        type=Path,
        default=Path("config/settings.yaml"),
        help="Pipeline settings YAML (mvp_mode true/false)",
    )
    parser.add_argument(
        "--recommendation-config",
        type=Path,
        default=Path("config/recommendation_v1.yaml"),
        help="Recommendation gate/grade YAML to verify or tune",
    )
    parser.add_argument(
        "--regime",
        choices=("current", "bull"),
        default="current",
        help="Market context: current cache indices or synthetic bull UP/UP",
    )
    parser.add_argument("--top-n", type=int, default=20)
    parser.add_argument("--target-min", type=int, default=10)
    parser.add_argument("--target-max", type=int, default=30)
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Skip grid sweep; validate current recommendation_v1.yaml gates only",
    )
    parser.add_argument("--output", type=Path, default=Path("output/threshold_tuning.json"))
    args = parser.parse_args()

    market_context = None
    if args.regime == "bull":
        market_context = {"kospi_trend": "UP", "kosdaq_trend": "UP", "market_trend": "UP"}

    inputs, meta = _collect_engine_inputs(
        args.universe,
        settings_path=args.settings,
        use_cache=not args.no_cache,
        market_context=market_context,
        gate_eligible_only=True,
    )
    if not inputs:
        print(json.dumps({"error": "No gate-eligible candidates evaluated", **meta}, indent=2))
        return 1

    matches = []
    if not args.verify_only:
        matches = sweep_thresholds(
            inputs,
            mvp_mode=bool(meta.get("mvp_mode", True)),
            recommendation_config_path=args.recommendation_config,
            top_n=args.top_n,
            target_min=args.target_min,
            target_max=args.target_max,
        )

    current_cfg = load_recommendation_config(path=args.recommendation_config).gates
    current_pool, current_picks = _count_picks(
        inputs,
        current_cfg,
        args.top_n,
        args.recommendation_config,
    )

    report = {
        "universe": str(args.universe),
        "settings": str(args.settings),
        "recommendation_config": str(args.recommendation_config),
        "mvp_mode": bool(meta.get("mvp_mode", True)),
        "regime": args.regime,
        "evaluated": meta["evaluated"],
        "gate_eligible": meta["gate_eligible"],
        "market_context": meta["market_context"],
        "target_pool": [args.target_min, args.target_max],
        "top_n": args.top_n,
        "current_config": {
            "pool": current_pool,
            "picks": current_picks,
            "gates": {
                "master_score_min": current_cfg.master_score_min,
                "probability_min": current_cfg.probability_min,
                "confidence_min": current_cfg.confidence_min,
                "risk_max": current_cfg.risk_max,
                "max_composite_failures": current_cfg.max_composite_failures,
            },
        },
        "matches_found": len(matches),
        "best": matches[0] if matches else None,
        "top_5": matches[:5],
        "recommendation_bottleneck": current_pool < meta["gate_eligible"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    # Success if current config is healthy OR sweep found alternatives
    target_picks = min(args.top_n, meta["gate_eligible"])
    min_expected_picks = max(1, min(args.target_min, target_picks))
    ok = bool(matches) or (
        current_picks >= min_expected_picks
        and args.target_min <= current_pool <= args.target_max
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
