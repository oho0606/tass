"""Generate TR0005–TR0080 catalog rule files and registry."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TR_DIR = ROOT / "engine" / "rules" / "tr"
CATALOG = ROOT / "rules" / "catalog" / "TR_v1.0.yaml"

HANDCRAFTED = {
    "TR0001": ("engine.rules.tr.tr0001_higher_high", "evaluate_higher_high"),
    "TR0002": ("engine.rules.tr.atomic", "evaluate_higher_low"),
    "TR0003": ("engine.rules.tr.atomic", "evaluate_lower_high"),
    "TR0004": ("engine.rules.tr.atomic", "evaluate_lower_low"),
}


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def _write_spec_rule(rule_id: str, rule_name: str) -> None:
    slug = _slug(rule_name)
    class_safe = re.sub(r"[^A-Za-z0-9]", "", rule_id + rule_name)
    content = f'''"""{rule_id} — {rule_name}. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class {class_safe}Rule(TrendSpecRule):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"


def evaluate_{rule_id.lower()}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return run_trend_spec_rule({class_safe}Rule, df)
'''
    (TR_DIR / f"{rule_id.lower()}_{slug}.py").write_text(content, encoding="utf-8")


def _load_rules() -> list[tuple[str, str]]:
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    rules: list[tuple[str, str]] = []
    for sub in data.get("subcategories", []):
        for rule in sub.get("rules", []):
            rules.append((rule["id"], rule["name"]))
    return rules


def main() -> None:
    TR_DIR.mkdir(parents=True, exist_ok=True)
    rules = _load_rules()
    imports: list[str] = []
    entries: list[str] = []

    for rule_id, rule_name in rules:
        if rule_id in HANDCRAFTED:
            module, fn = HANDCRAFTED[rule_id]
            imports.append(f"from {module} import {fn} as evaluate_{rule_id.lower()}")
        else:
            _write_spec_rule(rule_id, rule_name)
            slug = _slug(rule_name)
            module = f"engine.rules.tr.{rule_id.lower()}_{slug}"
            imports.append(f"from {module} import evaluate_{rule_id.lower()}")
        entries.append(f'    "{rule_id}": evaluate_{rule_id.lower()},')

    registry = f'''"""TR rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
{chr(10).join(imports)}

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

TR_EVALUATORS: dict[str, RuleEvaluator] = {{
{chr(10).join(entries)}
}}


def get_tr_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for TR rule ID."""
    return TR_EVALUATORS[rule_id]
'''
    (TR_DIR / "registry.py").write_text(registry, encoding="utf-8")
    print(f"TR registry: {len(rules)} rules")


if __name__ == "__main__":
    main()
