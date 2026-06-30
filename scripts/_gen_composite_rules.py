"""Generate composite catalog rules (CMA–CDQ) and registry."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
COMPOSITE_DIR = ROOT / "engine" / "rules" / "composite"
CATALOG = ROOT / "rules" / "catalog" / "Composite_v1.0.yaml"
HANDCRAFTED_PREFIX = "CTR"


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def _write_ratio_rule(rule_id: str, rule_name: str, atomic_prefix: str, mode: str) -> None:
    slug = _slug(rule_name)
    fn = f"evaluate_{rule_id.lower()}"
    content = f'''"""{rule_id} — {rule_name}. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="{rule_id}",
    rule_name="{rule_name}",
    atomic_prefix="{atomic_prefix}",
    mode="{mode}",
)


def {fn}(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate {rule_id} from atomic rule results."""
    return _RULE.evaluate(atomic)
'''
    (COMPOSITE_DIR / f"{rule_id.lower()}_{slug}.py").write_text(content, encoding="utf-8")


def _load_rules() -> list[tuple[str, str, str]]:
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    rules: list[tuple[str, str, str]] = []
    for category in data.get("composite_categories", []):
        atomic_prefix = category["atomic_category"]
        for sub in category.get("subcategories", []):
            for rule in sub.get("rules", []):
                rules.append((rule["id"], rule["name"], atomic_prefix))
    return rules


def main() -> None:
    from engine.rules.composite._ratio import infer_composite_mode

    rules = _load_rules()
    imports: list[str] = []
    entries: list[str] = []

    for rule_id, rule_name, atomic_prefix in rules:
        if rule_id.startswith(HANDCRAFTED_PREFIX):
            module = "engine.rules.composite.ctr"
            fn = f"evaluate_{rule_id.lower()}"
            imports.append(f"from {module} import {fn}")
            entries.append(f'    "{rule_id}": {fn},')
            continue

        mode = infer_composite_mode(rule_name)
        _write_ratio_rule(rule_id, rule_name, atomic_prefix, mode)
        slug = _slug(rule_name)
        module = f"engine.rules.composite.{rule_id.lower()}_{slug}"
        fn = f"evaluate_{rule_id.lower()}"
        imports.append(f"from {module} import {fn}")
        entries.append(f'    "{rule_id}": {fn},')

    registry = f'''"""Composite rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

from engine.core.types import RuleResult
from engine.rules.composite.ctr import evaluate_ctr_rules
{chr(10).join(imports)}

CompositeEvaluator = Callable[[dict[str, RuleResult]], RuleResult]

COMPOSITE_EVALUATORS: dict[str, CompositeEvaluator] = {{
{chr(10).join(entries)}
}}


def evaluate_composite(rule_id: str, atomic: dict[str, RuleResult]) -> RuleResult:
    evaluator = COMPOSITE_EVALUATORS.get(rule_id)
    if evaluator is None:
        return RuleResult(
            rule_id=rule_id,
            verdict="UNKNOWN",
            status="UNKNOWN",
            score=0.0,
            reasons=[f"Composite rule not implemented: {{rule_id}}"],
            metadata={{"not_implemented": True}},
        )
    return evaluator(atomic)


def evaluate_composites(
    rule_ids: list[str], atomic: dict[str, RuleResult]
) -> dict[str, RuleResult]:
    return {{rid: evaluate_composite(rid, atomic) for rid in rule_ids}}


__all__ = [
    "COMPOSITE_EVALUATORS",
    "evaluate_composite",
    "evaluate_composites",
    "evaluate_ctr_rules",
]
'''
    (COMPOSITE_DIR / "registry.py").write_text(registry, encoding="utf-8")
    generated = sum(1 for rid, _, _ in rules if not rid.startswith(HANDCRAFTED_PREFIX))
    print(f"Composite registry: {len(rules)} rules ({generated} generated)")


if __name__ == "__main__":
    main()
