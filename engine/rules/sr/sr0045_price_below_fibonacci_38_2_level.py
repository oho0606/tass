"""SR0045 — Price Below Fibonacci 38.2 Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0045PriceBelowFibonacci382LevelRule(SpecRule):
    rule_id = "SR0045"
    rule_name = "Price Below Fibonacci 38.2 Level"


def evaluate_sr0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0045."""
    return run_spec_rule(SR0045PriceBelowFibonacci382LevelRule, df)
