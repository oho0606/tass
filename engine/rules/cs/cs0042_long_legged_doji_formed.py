"""CS0042 — Long Legged Doji Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0042LongLeggedDojiFormedRule(SpecRule):
    rule_id = "CS0042"
    rule_name = "Long Legged Doji Formed"


def evaluate_cs0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0042."""
    return run_spec_rule(CS0042LongLeggedDojiFormedRule, df)
