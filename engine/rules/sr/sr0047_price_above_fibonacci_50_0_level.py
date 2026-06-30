"""SR0047 — Price Above Fibonacci 50.0 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0047PriceAboveFibonacci500LevelRule(SpecRule):
    rule_id = "SR0047"
    rule_name = "Price Above Fibonacci 50.0 Level"


def evaluate_sr0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0047."""
    return run_spec_rule(SR0047PriceAboveFibonacci500LevelRule, df)
