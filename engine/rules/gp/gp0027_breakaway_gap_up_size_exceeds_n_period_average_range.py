"""GP0027 — Breakaway Gap Up Size Exceeds N-Period Average Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0027BreakawayGapUpSizeExceedsNPeriodAverageRangeRule(SpecRule):
    rule_id = "GP0027"
    rule_name = "Breakaway Gap Up Size Exceeds N-Period Average Range"


def evaluate_gp0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0027."""
    return run_spec_rule(GP0027BreakawayGapUpSizeExceedsNPeriodAverageRangeRule, df)
