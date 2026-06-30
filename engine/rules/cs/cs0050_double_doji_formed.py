"""CS0050 — Double Doji Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0050DoubleDojiFormedRule(SpecRule):
    rule_id = "CS0050"
    rule_name = "Double Doji Formed"


def evaluate_cs0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0050."""
    return run_spec_rule(CS0050DoubleDojiFormedRule, df)
