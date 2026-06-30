#!/usr/bin/env python3
"""Run MVP rule universe backtests and promote lifecycle to Adopted/Rejected."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

MVP_CONFIG = ROOT / "config" / "mvp_operational_rules.yaml"
RULE_DB_DIR = ROOT / "rule_database" / "rules"

from engine.application.market_data_loader import load_universe_ohlcv
from engine.backtest.config import load_backtest_config
from engine.backtest.registry import get_rule_evaluator
from engine.backtest.rule_backtest import backtest_rule
from engine.core.rule_database import RuleDatabase
from engine.indicators.registry import compute_all


def _utc_now() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_mvp_rule_ids() -> list[str]:
    with MVP_CONFIG.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    keys = ("trend_atomic", "trend_composite", "moving_average", "volume")
    return [rule_id for key in keys for rule_id in cfg.get(key, [])]


def _lifecycle_from_verdict(verdict: str) -> str:
    mapping = {
        "ADOPT": "Adopted",
        "REJECT": "Rejected",
        "REVISE": "Implemented",
        "INSUFFICIENT_DATA": "Implemented",
    }
    return mapping.get(verdict, "Implemented")


def _aggregate_verdict(verdicts: list[str]) -> str:
    if not verdicts:
        return "INSUFFICIENT_DATA"
    adopt = verdicts.count("ADOPT")
    reject = verdicts.count("REJECT")
    if adopt >= max(2, len(verdicts) // 3):
        return "ADOPT"
    if reject >= len(verdicts) * 2 // 3:
        return "REJECT"
    if verdicts.count("REVISE") >= adopt:
        return "REVISE"
    return "REVISE"


def adopt_mvp_rules(
    *,
    universe: Path,
    max_symbols: int = 20,
    min_cached_symbols: int = 3,
    dry_run: bool = False,
) -> dict:
    """Backtest MVP rules across cached universe and update lifecycle."""
    rule_ids = _load_mvp_rule_ids()
    cfg = load_backtest_config()

    load_result = load_universe_ohlcv(
        universe,
        use_cache=True,
        fetch_missing=False,
        min_bars=cfg.evaluation.min_bars,
        compute_indicators=False,
    )
    symbols = list(load_result.ohlcv_by_symbol.keys())[:max_symbols]
    if len(symbols) < min_cached_symbols:
        return {
            "passed": False,
            "error": "insufficient_cache",
            "cached_symbols": len(symbols),
            "required": min_cached_symbols,
            "skipped_symbols": list(load_result.skipped_symbols),
        }

    db = RuleDatabase()
    report_rules: list[dict] = []

    for rule_id in rule_ids:
        db.upsert_from_folder(rule_id)
        symbol_results: list[dict] = []
        verdicts: list[str] = []

        try:
            evaluator = get_rule_evaluator(rule_id)
        except Exception as exc:  # noqa: BLE001
            report_rules.append(
                {
                    "rule_id": rule_id,
                    "error": str(exc),
                    "aggregate_verdict": "INSUFFICIENT_DATA",
                    "lifecycle": "Implemented",
                }
            )
            continue

        for symbol in symbols:
            try:
                df = compute_all(load_result.ohlcv_by_symbol[symbol].copy())
            except Exception as exc:  # noqa: BLE001
                symbol_results.append({"symbol": symbol, "error": str(exc), "skipped": True})
                continue
            result = backtest_rule(rule_id, symbol, df, evaluator, cfg)
            verdicts.append(result.verdict)
            symbol_results.append(
                {
                    "symbol": symbol,
                    "verdict": result.verdict,
                    "win_rate": round(result.metrics.win_rate, 4),
                    "profit_factor": round(result.metrics.profit_factor, 4),
                    "trade_count": result.metrics.trade_count,
                    "max_drawdown_pct": round(result.metrics.max_drawdown_pct, 2),
                }
            )

        aggregate = _aggregate_verdict(verdicts)
        lifecycle = _lifecycle_from_verdict(aggregate)

        rule_dir = RULE_DB_DIR / rule_id
        meta_path = rule_dir / "metadata.json"
        if meta_path.exists():
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            meta["backtest_verdict"] = aggregate
            meta["lifecycle_stage"] = lifecycle
            meta["backtest_evaluated_at"] = _utc_now()
            meta["backtest_symbols"] = len(symbols)
            if not dry_run:
                meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        summary_path = rule_dir / "backtest_summary.json"
        summary = {
            "rule_id": rule_id,
            "evaluated_at": _utc_now(),
            "universe": str(universe),
            "symbols_tested": symbols,
            "aggregate_verdict": aggregate,
            "lifecycle": lifecycle,
            "per_symbol": symbol_results,
        }
        if not dry_run:
            summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            db.set_lifecycle_stage(rule_id, lifecycle)

        report_rules.append(summary)

    adopted = sum(1 for r in report_rules if r.get("lifecycle") == "Adopted")
    rejected = sum(1 for r in report_rules if r.get("lifecycle") == "Rejected")
    db.close()

    return {
        "passed": adopted > 0,
        "rules_evaluated": len(report_rules),
        "adopted": adopted,
        "rejected": rejected,
        "cached_symbols": len(symbols),
        "rules": report_rules,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="MVP rule backtest adoption workflow")
    parser.add_argument(
        "--universe",
        type=Path,
        default=Path("config/universe_krx_backtest.csv"),
    )
    parser.add_argument("--max-symbols", type=int, default=20)
    parser.add_argument("--output", type=Path, default=Path("output/mvp_adoption_report.json"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    report = adopt_mvp_rules(
        universe=args.universe,
        max_symbols=args.max_symbols,
        dry_run=args.dry_run,
    )
    if not args.dry_run:
        from engine.core.adopted_rules import clear_adopted_rules_cache
        from engine.core.mvp_adoption import finalize_non_adopted_rules

        finalize_non_adopted_rules(report, dry_run=False)
        clear_adopted_rules_cache()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(
        {
            "passed": report.get("passed"),
            "adopted": report.get("adopted"),
            "rejected": report.get("rejected"),
            "rules_evaluated": report.get("rules_evaluated"),
            "cached_symbols": report.get("cached_symbols"),
            "error": report.get("error"),
        },
        ensure_ascii=False,
        indent=2,
    ))
    if report.get("error"):
        return 1
    return 0 if report.get("passed") else 1


if __name__ == "__main__":
    raise SystemExit(main())
