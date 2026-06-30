"""TR0049 — Trend Duration Long. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0049TrendDurationLongRule(TrendSpecRule):
    rule_id = "TR0049"
    rule_name = "Trend Duration Long"


def evaluate_tr0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0049."""
    return run_trend_spec_rule(TR0049TrendDurationLongRule, df)
