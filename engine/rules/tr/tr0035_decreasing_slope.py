"""TR0035 — Decreasing Slope. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0035DecreasingSlopeRule(TrendSpecRule):
    rule_id = "TR0035"
    rule_name = "Decreasing Slope"


def evaluate_tr0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0035."""
    return run_trend_spec_rule(TR0035DecreasingSlopeRule, df)
