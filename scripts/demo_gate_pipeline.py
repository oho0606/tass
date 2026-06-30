#!/usr/bin/env python3
"""Demo: run Gate Pipeline end-to-end and print results."""

from __future__ import annotations

import json
from pathlib import Path

from engine.application import RecommendationService, format_daily_picks_summary
from engine.application.settings import load_pipeline_settings
from engine.data.engine import DataEngine
from engine.data.universe import load_universe
from engine.domains.moving_average_engine import evaluate_moving_average_engine
from engine.domains.trend_engine import evaluate_trend_engine
from engine.domains.volume_engine import evaluate_volume_engine
from engine.gate.evaluate import evaluate_symbol_gates
from engine.gate.market_context import load_market_context
from engine.indicators.registry import compute_all
from engine.recommendation.top20 import build_candidate
from engine.scoring import compute_master_score


def main() -> int:
    settings = load_pipeline_settings()
    data_engine = DataEngine(settings.to_data_engine_config())
    gate_cfg = settings.to_gate_config()
    universe_path = Path("config/universe_sample.csv")

    print("=== 1. Market Context (KOSPI/KOSDAQ) ===")
    market = load_market_context(data_engine, use_cache=True)
    print(json.dumps(market, indent=2, ensure_ascii=False))

    print("\n=== 2. Symbol Gate Evaluation (first 3) ===")
    universe = load_universe(universe_path)
    candidates = []
    for entry in universe[:3]:
        yahoo_sym = data_engine.adapter.to_yahoo_symbol(entry.symbol, entry.market)
        df, validation = data_engine.get_ohlcv(yahoo_sym, use_cache=True)
        if df.empty:
            print(f"  {entry.symbol} {entry.name}: SKIP (no data)")
            continue
        df = compute_all(df)
        trend = evaluate_trend_engine(df)
        master = compute_master_score(
            trend=trend,
            moving_average=evaluate_moving_average_engine(df),
            volume=evaluate_volume_engine(df),
            mvp_mode=True,
        )
        gate_eval = evaluate_symbol_gates(
            df=df,
            trend=trend,
            data_valid=validation.valid,
            gate_cfg=gate_cfg,
            master=master,
            market_context=market,
        )
        master = gate_eval.adjusted_master or master
        print(f"\n  {entry.name} ({entry.symbol})")
        print(f"    Score: {master.total_score:.0f} | Gate: {gate_eval.gate_status}")
        for report in gate_eval.gate_report:
            line = f"    [{report['status']}] {report['gate_name']}: {report['reason']}"
            if report.get("deduction"):
                line += f" (-{report['deduction']})"
            print(line)
        candidates.append(
            build_candidate(
                entry,
                master,
                trend,
                gate_eval.gate_status,
                df=df,
                gate=gate_eval.legacy_gate,
                data_valid=validation.valid,
                pipeline_gate_report=gate_eval.gate_report,
            )
        )

    print("\n=== 3. Full Daily Picks (10 symbols) ===")
    service = RecommendationService()
    result = service.generate_daily_picks(
        universe_path,
        use_cache=True,
        market_context=market,
    )
    result = service.save_daily_picks(result)
    print(format_daily_picks_summary(result))

    if result.picks:
        pick = result.picks[0]
        print("\n=== 4. Top Pick Gate Report (pipeline + recommendation) ===")
        for report in pick.gate_report or []:
            source = report.get("source", "recommendation")
            print(f"  [{report['status']}] ({source}) {report['gate_name']}: {report['reason']}")
    else:
        print("\n=== 4. No ranked picks (Market CRASH — retry with UP market) ===")
        up_market = {"kospi_trend": "UP", "kosdaq_trend": "UP", "market_trend": "UP"}
        up_result = service.generate_daily_picks(
            universe_path,
            use_cache=True,
            market_context=up_market,
        )
        print(f"  With UP market override: {len(up_result.picks)} picks")
        if up_result.picks:
            pick = up_result.picks[0]
            print(f"  Top: {pick.name} ({pick.symbol}) score={pick.total_score:.0f} gate={pick.gate}")
            print("  Pipeline gate report:")
            for report in (pick.gate_report or [])[:5]:
                if report.get("source") == "pipeline":
                    print(f"    [{report['status']}] {report['gate_name']}: {report['reason']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
