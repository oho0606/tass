"""TR0075 — Trend Restarting. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0075TrendRestartingRule(TrendSpecRule):
    rule_id = "TR0075"
    rule_name = "Trend Restarting"


def evaluate_tr0075(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0075."""
    return run_trend_spec_rule(TR0075TrendRestartingRule, df)
