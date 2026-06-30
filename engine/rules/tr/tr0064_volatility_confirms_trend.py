"""TR0064 — Volatility Confirms Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0064VolatilityConfirmsTrendRule(TrendSpecRule):
    rule_id = "TR0064"
    rule_name = "Volatility Confirms Trend"


def evaluate_tr0064(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0064."""
    return run_trend_spec_rule(TR0064VolatilityConfirmsTrendRule, df)
