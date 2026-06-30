#!/usr/bin/env python3
"""Verify MVP domain engines score only Adopted rules (Phase 6 accuracy check)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import yaml

from engine.core.adopted_rules import filter_adopted_weights, load_adopted_mvp_rule_ids
from engine.domains.trend_engine import ATOMIC_WEIGHTS, COMPOSITE_WEIGHTS
from engine.rules.ma.registry import MA_ENGINE_WEIGHTS
from engine.rules.vl.registry import VL_ENGINE_WEIGHTS

MVP_CONFIG = ROOT / "config" / "mvp_operational_rules.yaml"


def _load_mvp_ids() -> list[str]:
    with MVP_CONFIG.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    keys = ("trend_atomic", "trend_composite", "moving_average", "volume")
    return [rule_id for key in keys for rule_id in cfg.get(key, [])]


def verify_adopted_scoring() -> dict:
    adopted = load_adopted_mvp_rule_ids()
    mvp_ids = set(_load_mvp_ids())
    checks: list[dict] = []

    weight_maps = {
        "trend_atomic": ATOMIC_WEIGHTS,
        "trend_composite": COMPOSITE_WEIGHTS,
        "moving_average": MA_ENGINE_WEIGHTS,
        "volume": VL_ENGINE_WEIGHTS,
    }

    for domain, weights in weight_maps.items():
        filtered = filter_adopted_weights(weights, adopted)
        excluded = sorted(set(weights) - set(filtered))
        checks.append(
            {
                "name": f"{domain}_runtime_filter",
                "passed": set(filtered).issubset(adopted)
                and all(rule not in adopted for rule in excluded),
                "detail": f"active={sorted(filtered)} excluded={excluded}",
            }
        )

    rejected = sorted(mvp_ids - adopted)
    checks.append(
        {
            "name": "adopted_count",
            "passed": len(adopted) >= 1,
            "detail": f"{len(adopted)} adopted / {len(mvp_ids)} mvp; rejected={rejected}",
        }
    )

    passed = all(item["passed"] for item in checks)
    return {"passed": passed, "adopted": sorted(adopted), "rejected": rejected, "checks": checks}


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify adopted-only MVP scoring")
    parser.add_argument("--output", type=Path, default=Path("output/adopted_scoring_verify.json"))
    args = parser.parse_args()

    report = verify_adopted_scoring()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
