"""DQ0013 — Open Outside High Low Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0013OpenOutsideHighLowRangeRule(SpecRule):
    rule_id = "DQ0013"
    rule_name = "Open Outside High Low Range"


def evaluate_dq0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0013."""
    return run_spec_rule(DQ0013OpenOutsideHighLowRangeRule, df)
