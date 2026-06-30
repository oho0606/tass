"""TR0063 — Momentum Confirms Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0063MomentumConfirmsTrendRule(TrendSpecRule):
    rule_id = "TR0063"
    rule_name = "Momentum Confirms Trend"


def evaluate_tr0063(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0063."""
    return run_trend_spec_rule(TR0063MomentumConfirmsTrendRule, df)
