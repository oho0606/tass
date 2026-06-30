"""PA0034 — Range Smaller Than Prior Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0034RangeSmallerThanPriorRangeRule(SpecRule):
    rule_id = "PA0034"
    rule_name = "Range Smaller Than Prior Range"


def evaluate_pa0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0034."""
    return run_spec_rule(PA0034RangeSmallerThanPriorRangeRule, df)
