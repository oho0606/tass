"""SR0042 — Price Below Fibonacci 23.6 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0042PriceBelowFibonacci236LevelRule(SpecRule):
    rule_id = "SR0042"
    rule_name = "Price Below Fibonacci 23.6 Level"


def evaluate_sr0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0042."""
    return run_spec_rule(SR0042PriceBelowFibonacci236LevelRule, df)
