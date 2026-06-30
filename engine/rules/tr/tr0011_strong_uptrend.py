"""TR0011 — Strong Uptrend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0011StrongUptrendRule(TrendSpecRule):
    rule_id = "TR0011"
    rule_name = "Strong Uptrend"


def evaluate_tr0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0011."""
    return run_trend_spec_rule(TR0011StrongUptrendRule, df)
