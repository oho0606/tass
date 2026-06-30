"""Regenerate engine/rules/vl/registry.py from rule files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "engine" / "rules" / "vl"

ENGINE_RULES = (
    "VL0001",
    "VL0004",
    "VL0021",
    "VL0041",
    "VL0027",
    "VL0059",
)

ENGINE_WEIGHTS = {
    "VL0001": 1.20,
    "VL0004": 1.00,
    "VL0021": 1.10,
    "VL0041": 1.20,
    "VL0027": 1.10,
    "VL0059": 1.00,
}


def main() -> None:
    imports: list[str] = []
    entries: list[str] = []
    for path in sorted(ROOT.glob("vl*.py")):
        if path.name.startswith("_"):
            continue
        rule_id = path.name.split("_")[0].upper()
        fn = f"evaluate_{rule_id.lower()}"
        module = f"engine.rules.vl.{path.stem}"
        imports.append(f"from {module} import {fn}")
        entries.append(f'    "{rule_id}": {fn},')

    weights_lines = "\n".join(f'    "{k}": {v},' for k, v in ENGINE_WEIGHTS.items())
    engine_rules = ",\n    ".join(f'"{r}"' for r in ENGINE_RULES)

    content = f'''"""VL rule evaluator registry."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
{chr(10).join(imports)}

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

VL_EVALUATORS: dict[str, RuleEvaluator] = {{
{chr(10).join(entries)}
}}

VL_ENGINE_RULES: tuple[str, ...] = (
    {engine_rules},
)

VL_ENGINE_WEIGHTS: dict[str, float] = {{
{weights_lines}
}}


def get_vl_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for VL rule ID."""
    return VL_EVALUATORS[rule_id]
'''
    (ROOT / "registry.py").write_text(content, encoding="utf-8")
    print(f"registry updated with {len(entries)} rules")


if __name__ == "__main__":
    main()
