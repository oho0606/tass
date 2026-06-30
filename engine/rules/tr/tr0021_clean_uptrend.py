"""TR0021 — Clean Uptrend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0021CleanUptrendRule(TrendSpecRule):
    rule_id = "TR0021"
    rule_name = "Clean Uptrend"


def evaluate_tr0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0021."""
    return run_trend_spec_rule(TR0021CleanUptrendRule, df)
