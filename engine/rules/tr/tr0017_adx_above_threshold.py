"""TR0017 — ADX Above Threshold. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0017ADXAboveThresholdRule(TrendSpecRule):
    rule_id = "TR0017"
    rule_name = "ADX Above Threshold"


def evaluate_tr0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0017."""
    return run_trend_spec_rule(TR0017ADXAboveThresholdRule, df)
