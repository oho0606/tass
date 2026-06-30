"""SR0046 — Price At Fibonacci 38.2 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0046PriceAtFibonacci382LevelRule(SpecRule):
    rule_id = "SR0046"
    rule_name = "Price At Fibonacci 38.2 Level"


def evaluate_sr0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0046."""
    return run_spec_rule(SR0046PriceAtFibonacci382LevelRule, df)
