"""TR0038 — Slope Breakout. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0038SlopeBreakoutRule(TrendSpecRule):
    rule_id = "TR0038"
    rule_name = "Slope Breakout"


def evaluate_tr0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0038."""
    return run_trend_spec_rule(TR0038SlopeBreakoutRule, df)
