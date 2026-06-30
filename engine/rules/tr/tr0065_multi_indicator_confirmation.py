"""TR0065 — Multi Indicator Confirmation. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0065MultiIndicatorConfirmationRule(TrendSpecRule):
    rule_id = "TR0065"
    rule_name = "Multi Indicator Confirmation"


def evaluate_tr0065(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0065."""
    return run_trend_spec_rule(TR0065MultiIndicatorConfirmationRule, df)
