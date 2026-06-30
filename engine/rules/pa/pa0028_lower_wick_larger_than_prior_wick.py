"""PA0028 — Lower Wick Larger Than Prior Wick. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0028LowerWickLargerThanPriorWickRule(SpecRule):
    rule_id = "PA0028"
    rule_name = "Lower Wick Larger Than Prior Wick"


def evaluate_pa0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0028."""
    return run_spec_rule(PA0028LowerWickLargerThanPriorWickRule, df)
