"""TR0044 — Consecutive Lower Lows. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0044ConsecutiveLowerLowsRule(TrendSpecRule):
    rule_id = "TR0044"
    rule_name = "Consecutive Lower Lows"


def evaluate_tr0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0044."""
    return run_trend_spec_rule(TR0044ConsecutiveLowerLowsRule, df)
