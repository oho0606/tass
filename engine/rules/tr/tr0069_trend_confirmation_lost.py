"""TR0069 — Trend Confirmation Lost. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0069TrendConfirmationLostRule(TrendSpecRule):
    rule_id = "TR0069"
    rule_name = "Trend Confirmation Lost"


def evaluate_tr0069(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0069."""
    return run_trend_spec_rule(TR0069TrendConfirmationLostRule, df)
