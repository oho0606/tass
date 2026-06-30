"""SR0048 — Price Below Fibonacci 50.0 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0048PriceBelowFibonacci500LevelRule(SpecRule):
    rule_id = "SR0048"
    rule_name = "Price Below Fibonacci 50.0 Level"


def evaluate_sr0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0048."""
    return run_spec_rule(SR0048PriceBelowFibonacci500LevelRule, df)
