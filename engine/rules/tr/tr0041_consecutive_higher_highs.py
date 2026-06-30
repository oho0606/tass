"""TR0041 — Consecutive Higher Highs. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0041ConsecutiveHigherHighsRule(TrendSpecRule):
    rule_id = "TR0041"
    rule_name = "Consecutive Higher Highs"


def evaluate_tr0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0041."""
    return run_trend_spec_rule(TR0041ConsecutiveHigherHighsRule, df)
