"""TR0037 — Decelerating Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0037DeceleratingTrendRule(TrendSpecRule):
    rule_id = "TR0037"
    rule_name = "Decelerating Trend"


def evaluate_tr0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0037."""
    return run_trend_spec_rule(TR0037DeceleratingTrendRule, df)
