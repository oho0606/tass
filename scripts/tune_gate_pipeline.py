#!/usr/bin/env python3
"""Dry-run sweep for TASS-006 gate pipeline parameters (Phase 6 tuning).

Evaluates cached universe symbols and reports pipeline gate pass rates for
candidate ``gate_pipeline_v1.yaml`` settings.
"""

from __future__ import annotations

import argparse
import json
from copy import deepcopy
from dataclasses import replace
from itertools import product
from pathlib import Path

from engine.application.settings import load_pipeline_settings
from engine.data.engine import DataEngine
from engine.data.universe import load_universe
from engine.domains.moving_average_engine import evaluate_moving_average_engine
from engine.domains.trend_engine import evaluate_trend_engine
from engine.domains.volume_engine import evaluate_volume_engine
from engine.gate.config import GateConfig, merge_gate_config
from engine.gate.evaluate import evaluate_symbol_gates
from engine.gate.factory import build_gate_pipeline
from engine.gate.market_context import load_market_context
from engine.indicators.registry import compute_all
from engine.scoring import compute_master_score


def _evaluate_universe(
    universe_path: Path,
    *,
    gate_cfg: GateConfig,
    pipeline_gates: dict,
    use_cache: bool,
) -> tuple[list[dict], dict]:
    settings = load_pipeline_settings()
    data_engine = DataEngine(settings.to_data_engine_config())
    market_context = load_market_context(data_engine, use_cache=use_cache)
    universe = load_universe(universe_path)
    merged = merge_gate_config(pipeline_gates, gate_cfg)
    pipeline = build_gate_pipeline(merged)

    rows: list[dict] = []
    fail_counts: dict[str, int] = {}

    for entry in universe:
        yahoo_sym = data_engine.adapter.to_yahoo_symbol(entry.symbol, entry.market)
        df, validation = data_engine.get_ohlcv(yahoo_sym, use_cache=use_cache)
        if df.empty:
            continue

        df = compute_all(df)
        trend = evaluate_trend_engine(df)
        master = compute_master_score(
            trend=trend,
            moving_average=evaluate_moving_average_engine(df),
            volume=evaluate_volume_engine(df),
            mvp_mode=True,
        )
        evaluation = evaluate_symbol_gates(
            df=df,
            trend=trend,
            data_valid=validation.valid,
            gate_cfg=gate_cfg,
            master=master,
            pipeline=pipeline,
            market_context=market_context,
            listing_market=entry.market,
        )
        failed_gate = None
        if evaluation.pipeline_result.gate_results:
            for result in evaluation.pipeline_result.gate_results:
                if result.status.value == "FAIL":
                    failed_gate = result.name
                    fail_counts[failed_gate] = fail_counts.get(failed_gate, 0) + 1
                    break

        rows.append(
            {
                "symbol": entry.symbol,
                "market": entry.market,
                "gate_status": evaluation.gate_status,
                "failed_gate": failed_gate,
                "score": master.total_score,
            }
        )

    return rows, fail_counts


def _summarize(rows: list[dict], *, label: str, params: dict) -> dict:
    total = len(rows)
    passed = sum(1 for row in rows if row["gate_status"] == "PASS")
    warned = sum(1 for row in rows if row["gate_status"] == "WARN")
    failed = total - passed - warned
    top_pass = sum(1 for row in sorted(rows, key=lambda r: r["score"], reverse=True)[:20] if row["gate_status"] == "PASS")
    return {
        "label": label,
        "params": params,
        "evaluated": total,
        "pipeline_pass": passed,
        "pipeline_warn": warned,
        "pipeline_fail": failed,
        "pass_rate": round(passed / total, 3) if total else 0.0,
        "top20_pass": top_pass,
    }


def sweep_configs(
    universe_path: Path,
    *,
    gate_cfg: GateConfig,
    base_gates: dict,
    use_cache: bool,
) -> list[dict]:
    scenarios: list[tuple[str, dict]] = []

    for combine_mode in ("worst", "listing"):
        gates = deepcopy(base_gates)
        gates.setdefault("market", {})["combine_mode"] = combine_mode
        scenarios.append((f"combine_mode={combine_mode}", gates))

    for crash_drawdown in (0.08, 0.10, 0.12, 0.15):
        gates = deepcopy(base_gates)
        gates.setdefault("market", {})["combine_mode"] = "listing"
        gates["market"]["crash_drawdown"] = crash_drawdown
        scenarios.append((f"listing+crash_drawdown={crash_drawdown}", gates))

    for floor in (80, 100, 120):
        gates = deepcopy(base_gates)
        gates.setdefault("market", {})["combine_mode"] = "listing"
        scenarios.append((f"listing+trend_floor={floor}", gates))

    results: list[dict] = []
    seen: set[str] = set()
    for label, gates in scenarios:
        if label in seen:
            continue
        seen.add(label)
        local_cfg = gate_cfg
        local_gates = gates
        params = {
            "combine_mode": local_gates.get("market", {}).get("combine_mode", "worst"),
            "crash_drawdown": local_gates.get("market", {}).get("crash_drawdown", 0.08),
            "trend_floor_score": local_cfg.trend_floor_score,
        }
        if "trend_floor=" in label:
            floor = int(label.split("=")[-1])
            local_cfg = replace(gate_cfg, trend_floor_score=float(floor))
            params["trend_floor_score"] = floor

        rows, fail_counts = _evaluate_universe(
            universe_path,
            gate_cfg=local_cfg,
            pipeline_gates=local_gates,
            use_cache=use_cache,
        )
        summary = _summarize(rows, label=label, params=params)
        summary["fail_by_gate"] = fail_counts
        results.append(summary)

    results.sort(key=lambda item: (-item["top20_pass"], -item["pipeline_pass"], item["pipeline_fail"]))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Tune gate_pipeline_v1.yaml parameters")
    parser.add_argument("--universe", type=Path, default=Path("config/universe_krx_mvp.csv"))
    parser.add_argument("--config", type=Path, default=Path("config/settings.yaml"))
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument("--output", type=Path, default=Path("output/gate_tuning.json"))
    args = parser.parse_args()

    settings = load_pipeline_settings(args.config)
    from engine.gate.config import load_gate_pipeline_yaml

    base_gates = load_gate_pipeline_yaml()
    results = sweep_configs(
        args.universe,
        gate_cfg=settings.to_gate_config(),
        base_gates=base_gates,
        use_cache=not args.no_cache,
    )

    report = {
        "universe": str(args.universe),
        "evaluated_scenarios": len(results),
        "best": results[0] if results else None,
        "top_5": results[:5],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
