#!/usr/bin/env python3
"""Phase 6 product validation: picks quality, SSOT, cache, adoption checks."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

RECOMMENDABLE = frozenset({"STRONG BUY", "BUY", "WATCHLIST", "HOLD"})


def _latest_picks(path: Path | None) -> Path | None:
    if path is not None:
        return path if path.exists() else None
    candidates = sorted((ROOT / "output").glob("picks_*.json"))
    return candidates[-1] if candidates else None


def _count_cached_symbols(cache_dir: Path, universe_path: Path) -> int:
    from engine.application.market_data_loader import load_universe_ohlcv

    result = load_universe_ohlcv(
        universe_path,
        use_cache=True,
        fetch_missing=False,
        min_bars=60,
        cache_dir=cache_dir,
    )
    return len(result.ohlcv_by_symbol)


def validate_phase6(
    *,
    picks_path: Path | None,
    universe: Path,
    cache_dir: Path,
    min_picks: int = 1,
    min_cached: int = 10,
) -> dict:
    checks: list[dict] = []
    picks_file = _latest_picks(picks_path)

    # 1. Picks file exists
    checks.append(
        {
            "name": "picks_file_exists",
            "passed": picks_file is not None,
            "detail": str(picks_file) if picks_file else "no picks_*.json in output/",
        }
    )

    payload: dict = {}
    if picks_file:
        payload = json.loads(picks_file.read_text(encoding="utf-8"))
        picks = payload.get("picks") or []

        checks.append(
            {
                "name": "picks_count",
                "passed": len(picks) >= min_picks,
                "detail": f"{len(picks)} picks (min {min_picks})",
            }
        )
        checks.append(
            {
                "name": "mvp_mode",
                "passed": payload.get("mvp_mode") is True,
                "detail": f"mvp_mode={payload.get('mvp_mode')}",
            }
        )

        explainable = 0
        for pick in picks:
            reasons = pick.get("recommendation_reason") or pick.get("reasons") or []
            has_score = pick.get("total_score", 0) > 0
            has_rec = pick.get("recommendation") in RECOMMENDABLE
            if reasons and has_score and has_rec:
                explainable += 1
        checks.append(
            {
                "name": "explainable_picks",
                "passed": explainable == len(picks) and len(picks) > 0,
                "detail": f"{explainable}/{len(picks)} with reasons+score+recommendation",
            }
        )

        recommendable = sum(1 for p in picks if p.get("recommendation") in RECOMMENDABLE)
        checks.append(
            {
                "name": "recommendation_assignments",
                "passed": recommendable == len(picks) and len(picks) > 0,
                "detail": f"{recommendable}/{len(picks)} with actionable recommendation",
            }
        )

        gate_pass = sum(1 for p in picks if (p.get("gate") or "").upper() == "PASS")
        gate_fail_in_picks = sum(1 for p in picks if (p.get("gate") or "").upper() == "FAIL")
        checks.append(
            {
                "name": "picks_gate_eligible",
                "passed": gate_fail_in_picks == 0,
                "detail": f"{len(picks) - gate_fail_in_picks}/{len(picks)} picks without pipeline gate FAIL",
            }
        )
        checks.append(
            {
                "name": "pipeline_gate_pass_rate",
                "passed": True,
                "detail": f"{gate_pass}/{len(picks)} pipeline gate PASS (informational)",
            }
        )

        gate_blocked = payload.get("gate_blocked") or []
        if gate_blocked:
            checks.append(
                {
                    "name": "gate_blocked_observation",
                    "passed": True,
                    "detail": f"{len(gate_blocked)} gate-blocked candidates listed separately",
                }
            )

    # 2. Cache coverage
    cached = _count_cached_symbols(cache_dir, universe)
    checks.append(
        {
            "name": "cache_coverage",
            "passed": cached >= min_cached,
            "detail": f"{cached} symbols cached (min {min_cached})",
        }
    )

    # 3. SSOT verify script
    ssot = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_rule_ssot.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    checks.append(
        {
            "name": "mvp_ssot_verify",
            "passed": ssot.returncode == 0,
            "detail": (ssot.stdout or ssot.stderr).strip().splitlines()[-1] if ssot.stdout or ssot.stderr else "",
        }
    )

    # 4. Adoption report
    adoption_path = ROOT / "output" / "mvp_adoption_report.json"
    if adoption_path.exists():
        adoption = json.loads(adoption_path.read_text(encoding="utf-8"))
        adopted = adoption.get("adopted", 0)
        rejected = adoption.get("rejected", 0)
        checks.append(
            {
                "name": "mvp_rules_adopted",
                "passed": adopted >= 1,
                "detail": f"{adopted} adopted, {rejected} rejected",
            }
        )
        checks.append(
            {
                "name": "mvp_rules_resolved",
                "passed": adopted + rejected >= adoption.get("rules_evaluated", 0),
                "detail": f"{adopted + rejected}/{adoption.get('rules_evaluated', 0)} rules Adopted or Rejected",
            }
        )
    else:
        checks.append(
            {
                "name": "mvp_rules_adopted",
                "passed": False,
                "detail": "run scripts/adopt_mvp_rules.py first",
            }
        )

    passed = all(c["passed"] for c in checks if c["name"] != "pipeline_gate_pass_rate")
    return {
        "passed": passed,
        "picks_file": str(picks_file) if picks_file else None,
        "universe": str(universe),
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Phase 6 picks quality validation")
    parser.add_argument("--picks", type=Path, default=None)
    parser.add_argument("--universe", type=Path, default=Path("config/universe_krx_backtest.csv"))
    parser.add_argument("--cache-dir", type=Path, default=Path("data/cache"))
    parser.add_argument("--output", type=Path, default=Path("output/phase6_validation.json"))
    parser.add_argument("--min-picks", type=int, default=1)
    parser.add_argument("--min-cached", type=int, default=10)
    args = parser.parse_args()

    report = validate_phase6(
        picks_path=args.picks,
        universe=args.universe,
        cache_dir=args.cache_dir,
        min_picks=args.min_picks,
        min_cached=args.min_cached,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
