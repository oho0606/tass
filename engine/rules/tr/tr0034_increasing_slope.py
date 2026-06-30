"""TR0034 — Increasing Slope. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0034IncreasingSlopeRule(TrendSpecRule):
    rule_id = "TR0034"
    rule_name = "Increasing Slope"


def evaluate_tr0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0034."""
    return run_trend_spec_rule(TR0034IncreasingSlopeRule, df)
