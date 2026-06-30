"""TR0067 — Trend Confirmation Strong. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0067TrendConfirmationStrongRule(TrendSpecRule):
    rule_id = "TR0067"
    rule_name = "Trend Confirmation Strong"


def evaluate_tr0067(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0067."""
    return run_trend_spec_rule(TR0067TrendConfirmationStrongRule, df)
