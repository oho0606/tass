"""GP0033 — Continuation Gap Up Bar Bullish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0033ContinuationGapUpBarBullishRule(SpecRule):
    rule_id = "GP0033"
    rule_name = "Continuation Gap Up Bar Bullish"


def evaluate_gp0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0033."""
    return run_spec_rule(GP0033ContinuationGapUpBarBullishRule, df)
