"""TR0008 — Trend Reversal Up. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0008TrendReversalUpRule(TrendSpecRule):
    rule_id = "TR0008"
    rule_name = "Trend Reversal Up"


def evaluate_tr0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0008."""
    return run_trend_spec_rule(TR0008TrendReversalUpRule, df)
