"""TR0031 — Positive Slope. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0031PositiveSlopeRule(TrendSpecRule):
    rule_id = "TR0031"
    rule_name = "Positive Slope"


def evaluate_tr0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0031."""
    return run_trend_spec_rule(TR0031PositiveSlopeRule, df)
