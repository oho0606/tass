"""TR0072 — Trend Emerging. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0072TrendEmergingRule(TrendSpecRule):
    rule_id = "TR0072"
    rule_name = "Trend Emerging"


def evaluate_tr0072(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0072."""
    return run_trend_spec_rule(TR0072TrendEmergingRule, df)
