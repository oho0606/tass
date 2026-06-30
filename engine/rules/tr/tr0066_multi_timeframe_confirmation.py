"""TR0066 — Multi Timeframe Confirmation. TASS-014: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr._runtime import TrendSpecRule, run_trend_spec_rule


class TR0066MultiTimeframeConfirmationRule(TrendSpecRule):
    rule_id = "TR0066"
    rule_name = "Multi Timeframe Confirmation"


def evaluate_tr0066(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for TR0066."""
    return run_trend_spec_rule(TR0066MultiTimeframeConfirmationRule, df)
