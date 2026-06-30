"""SR0041 — Price Above Fibonacci 23.6 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0041PriceAboveFibonacci236LevelRule(SpecRule):
    rule_id = "SR0041"
    rule_name = "Price Above Fibonacci 23.6 Level"


def evaluate_sr0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0041."""
    return run_spec_rule(SR0041PriceAboveFibonacci236LevelRule, df)
