"""TR0026 — Stable Trend. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0026StableTrendRule(TrendSpecRule):
    rule_id = "TR0026"
    rule_name = "Stable Trend"


def evaluate_tr0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0026."""
    return run_trend_spec_rule(TR0026StableTrendRule, df)
