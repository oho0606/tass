"""VL0057 — Money Flow Positive. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import MoneyFlowRule, run_quality_rule


class VL0057MoneyFlowPositiveRule(MoneyFlowRule):
    rule_id = "VL0057"
    rule_name = "Money Flow Positive"
    direction = "positive"


def evaluate_vl0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0057."""
    return run_quality_rule(VL0057MoneyFlowPositiveRule, df)
