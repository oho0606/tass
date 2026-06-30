"""TR0048 — Trend Duration Medium. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0048TrendDurationMediumRule(TrendSpecRule):
    rule_id = "TR0048"
    rule_name = "Trend Duration Medium"


def evaluate_tr0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0048."""
    return run_trend_spec_rule(TR0048TrendDurationMediumRule, df)
