"""TR0053 — Buying Exhaustion. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0053BuyingExhaustionRule(TrendSpecRule):
    rule_id = "TR0053"
    rule_name = "Buying Exhaustion"


def evaluate_tr0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0053."""
    return run_trend_spec_rule(TR0053BuyingExhaustionRule, df)
