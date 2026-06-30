"""TR0042 — Consecutive Higher Lows. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0042ConsecutiveHigherLowsRule(TrendSpecRule):
    rule_id = "TR0042"
    rule_name = "Consecutive Higher Lows"


def evaluate_tr0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0042."""
    return run_trend_spec_rule(TR0042ConsecutiveHigherLowsRule, df)
