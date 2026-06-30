"""VL0058 — Money Flow Negative. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import MoneyFlowRule, run_quality_rule


class VL0058MoneyFlowNegativeRule(MoneyFlowRule):
    rule_id = "VL0058"
    rule_name = "Money Flow Negative"
    direction = "negative"


def evaluate_vl0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0058."""
    return run_quality_rule(VL0058MoneyFlowNegativeRule, df)
