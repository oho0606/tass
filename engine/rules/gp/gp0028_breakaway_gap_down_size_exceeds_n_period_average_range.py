"""GP0028 — Breakaway Gap Down Size Exceeds N-Period Average Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0028BreakawayGapDownSizeExceedsNPeriodAverageRangeRule(SpecRule):
    rule_id = "GP0028"
    rule_name = "Breakaway Gap Down Size Exceeds N-Period Average Range"


def evaluate_gp0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0028."""
    return run_spec_rule(GP0028BreakawayGapDownSizeExceedsNPeriodAverageRangeRule, df)
