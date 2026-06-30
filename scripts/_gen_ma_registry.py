"""Regenerate engine/rules/ma/registry.py from rule files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "engine" / "rules" / "ma"

ENGINE_RULES = (
    "MA0002",
    "MA0003",
    "MA0007",
    "MA0012",
    "MA0021",
    "MA0029",
)

ENGINE_WEIGHTS = {
    "MA0002": 1.20,
    "MA0003": 1.10,
    "MA0007": 0.90,
    "MA0012": 1.10,
    "MA0021": 1.30,
    "MA0029": 1.40,
}


def main() -> None:
    rule_ids = sorted(
        path.name.split("_")[0].upper()
        for path in ROOT.glob("ma*.py")
        if not path.name.startswith(("ma000", "ma00")) is False
    )
    # Collect from evaluate_* functions
    imports: list[str] = []
    entries: list[str] = []
    for path in sorted(ROOT.glob("ma*.py")):
        if path.name.startswith("_"):
            continue
        rule_id = path.name.split("_")[0].upper()
        fn = f"evaluate_{rule_id.lower()}"
        module = f"engine.rules.ma.{path.stem}"
        imports.append(f"from {module} import {fn}")
        entries.append(f'    "{rule_id}": {fn},')

    weights_lines = "\n".join(f'    "{k}": {v},' for k, v in ENGINE_WEIGHTS.items())
    engine_rules = ",\n    ".join(f'"{r}"' for r in ENGINE_RULES)

    content = f'''"""MA rule evaluator registry."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
{chr(10).join(imports)}

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

MA_EVALUATORS: dict[str, RuleEvaluator] = {{
{chr(10).join(entries)}
}}

MA_ENGINE_RULES: tuple[str, ...] = (
    {engine_rules},
)

MA_ENGINE_WEIGHTS: dict[str, float] = {{
{weights_lines}
}}


def get_ma_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for MA rule ID."""
    return MA_EVALUATORS[rule_id]
'''
    (ROOT / "registry.py").write_text(content, encoding="utf-8")
    print(f"registry updated with {len(entries)} rules")


if __name__ == "__main__":
    main()
