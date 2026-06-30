"""TR0025 — Noisy Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0025NoisyTrendRule(TrendSpecRule):
    rule_id = "TR0025"
    rule_name = "Noisy Trend"


def evaluate_tr0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0025."""
    return run_trend_spec_rule(TR0025NoisyTrendRule, df)
