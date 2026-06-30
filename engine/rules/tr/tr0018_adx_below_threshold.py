"""TR0018 — ADX Below Threshold. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0018ADXBelowThresholdRule(TrendSpecRule):
    rule_id = "TR0018"
    rule_name = "ADX Below Threshold"


def evaluate_tr0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0018."""
    return run_trend_spec_rule(TR0018ADXBelowThresholdRule, df)
