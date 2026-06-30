"""SR0050 — Price At Fibonacci 61.8 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0050PriceAtFibonacci618LevelRule(SpecRule):
    rule_id = "SR0050"
    rule_name = "Price At Fibonacci 61.8 Level"


def evaluate_sr0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0050."""
    return run_spec_rule(SR0050PriceAtFibonacci618LevelRule, df)
