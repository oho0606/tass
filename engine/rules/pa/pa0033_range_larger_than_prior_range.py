"""PA0033 — Range Larger Than Prior Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0033RangeLargerThanPriorRangeRule(SpecRule):
    rule_id = "PA0033"
    rule_name = "Range Larger Than Prior Range"


def evaluate_pa0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0033."""
    return run_spec_rule(PA0033RangeLargerThanPriorRangeRule, df)
