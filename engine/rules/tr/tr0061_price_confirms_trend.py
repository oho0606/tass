"""TR0061 — Price Confirms Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0061PriceConfirmsTrendRule(TrendSpecRule):
    rule_id = "TR0061"
    rule_name = "Price Confirms Trend"


def evaluate_tr0061(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0061."""
    return run_trend_spec_rule(TR0061PriceConfirmsTrendRule, df)
