"""TR0019 — Trend Momentum Increasing. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0019TrendMomentumIncreasingRule(TrendSpecRule):
    rule_id = "TR0019"
    rule_name = "Trend Momentum Increasing"


def evaluate_tr0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0019."""
    return run_trend_spec_rule(TR0019TrendMomentumIncreasingRule, df)
