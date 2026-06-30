"""TR0007 — Sideways Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0007SidewaysTrendRule(TrendSpecRule):
    rule_id = "TR0007"
    rule_name = "Sideways Trend"


def evaluate_tr0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0007."""
    return run_trend_spec_rule(TR0007SidewaysTrendRule, df)
