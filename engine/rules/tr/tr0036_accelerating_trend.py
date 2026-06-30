"""TR0036 — Accelerating Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0036AcceleratingTrendRule(TrendSpecRule):
    rule_id = "TR0036"
    rule_name = "Accelerating Trend"


def evaluate_tr0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0036."""
    return run_trend_spec_rule(TR0036AcceleratingTrendRule, df)
