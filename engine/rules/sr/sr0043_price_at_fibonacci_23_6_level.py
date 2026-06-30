"""SR0043 — Price At Fibonacci 23.6 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0043PriceAtFibonacci236LevelRule(SpecRule):
    rule_id = "SR0043"
    rule_name = "Price At Fibonacci 23.6 Level"


def evaluate_sr0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0043."""
    return run_spec_rule(SR0043PriceAtFibonacci236LevelRule, df)
