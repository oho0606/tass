"""TR0073 — Trend Maturing. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0073TrendMaturingRule(TrendSpecRule):
    rule_id = "TR0073"
    rule_name = "Trend Maturing"


def evaluate_tr0073(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0073."""
    return run_trend_spec_rule(TR0073TrendMaturingRule, df)
