"""TR0024 — Smooth Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0024SmoothTrendRule(TrendSpecRule):
    rule_id = "TR0024"
    rule_name = "Smooth Trend"


def evaluate_tr0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0024."""
    return run_trend_spec_rule(TR0024SmoothTrendRule, df)
