"""TR0068 — Trend Confirmation Weak. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0068TrendConfirmationWeakRule(TrendSpecRule):
    rule_id = "TR0068"
    rule_name = "Trend Confirmation Weak"


def evaluate_tr0068(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0068."""
    return run_trend_spec_rule(TR0068TrendConfirmationWeakRule, df)
