"""SR0049 — Price At Fibonacci 50.0 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0049PriceAtFibonacci500LevelRule(SpecRule):
    rule_id = "SR0049"
    rule_name = "Price At Fibonacci 50.0 Level"


def evaluate_sr0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0049."""
    return run_spec_rule(SR0049PriceAtFibonacci500LevelRule, df)
