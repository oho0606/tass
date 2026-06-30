"""GP0048 — Exhaustion Gap Down Bar Bullish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0048ExhaustionGapDownBarBullishRule(SpecRule):
    rule_id = "GP0048"
    rule_name = "Exhaustion Gap Down Bar Bullish"


def evaluate_gp0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0048."""
    return run_spec_rule(GP0048ExhaustionGapDownBarBullishRule, df)
