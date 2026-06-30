"""TR0013 — Strong Downtrend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0013StrongDowntrendRule(TrendSpecRule):
    rule_id = "TR0013"
    rule_name = "Strong Downtrend"


def evaluate_tr0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0013."""
    return run_trend_spec_rule(TR0013StrongDowntrendRule, df)
