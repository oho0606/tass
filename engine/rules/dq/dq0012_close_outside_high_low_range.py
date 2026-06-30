"""DQ0012 — Close Outside High Low Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0012CloseOutsideHighLowRangeRule(SpecRule):
    rule_id = "DQ0012"
    rule_name = "Close Outside High Low Range"


def evaluate_dq0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0012."""
    return run_spec_rule(DQ0012CloseOutsideHighLowRangeRule, df)
