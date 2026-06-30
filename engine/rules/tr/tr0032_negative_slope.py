"""TR0032 — Negative Slope. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0032NegativeSlopeRule(TrendSpecRule):
    rule_id = "TR0032"
    rule_name = "Negative Slope"


def evaluate_tr0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0032."""
    return run_trend_spec_rule(TR0032NegativeSlopeRule, df)
