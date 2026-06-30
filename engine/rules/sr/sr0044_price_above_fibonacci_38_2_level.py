"""SR0044 — Price Above Fibonacci 38.2 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0044PriceAboveFibonacci382LevelRule(SpecRule):
    rule_id = "SR0044"
    rule_name = "Price Above Fibonacci 38.2 Level"


def evaluate_sr0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0044."""
    return run_spec_rule(SR0044PriceAboveFibonacci382LevelRule, df)
