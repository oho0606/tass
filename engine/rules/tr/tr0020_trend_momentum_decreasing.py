"""TR0020 — Trend Momentum Decreasing. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0020TrendMomentumDecreasingRule(TrendSpecRule):
    rule_id = "TR0020"
    rule_name = "Trend Momentum Decreasing"


def evaluate_tr0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0020."""
    return run_trend_spec_rule(TR0020TrendMomentumDecreasingRule, df)
