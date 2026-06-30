"""TR0022 — Clean Downtrend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0022CleanDowntrendRule(TrendSpecRule):
    rule_id = "TR0022"
    rule_name = "Clean Downtrend"


def evaluate_tr0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0022."""
    return run_trend_spec_rule(TR0022CleanDowntrendRule, df)
