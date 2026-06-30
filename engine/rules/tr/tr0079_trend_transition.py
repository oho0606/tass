"""TR0079 — Trend Transition. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0079TrendTransitionRule(TrendSpecRule):
    rule_id = "TR0079"
    rule_name = "Trend Transition"


def evaluate_tr0079(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0079."""
    return run_trend_spec_rule(TR0079TrendTransitionRule, df)
