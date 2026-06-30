"""TR0040 — Slope Stability. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0040SlopeStabilityRule(TrendSpecRule):
    rule_id = "TR0040"
    rule_name = "Slope Stability"


def evaluate_tr0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0040."""
    return run_trend_spec_rule(TR0040SlopeStabilityRule, df)
