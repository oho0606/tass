"""CS0041 — Standard Doji Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0041StandardDojiFormedRule(SpecRule):
    rule_id = "CS0041"
    rule_name = "Standard Doji Formed"


def evaluate_cs0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0041."""
    return run_spec_rule(CS0041StandardDojiFormedRule, df)
