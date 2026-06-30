"""EX0024 — Exit Close Below EMA20 After Touch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0024ExitCloseBelowEMA20AfterTouchRule(SpecRule):
    rule_id = "EX0024"
    rule_name = "Exit Close Below EMA20 After Touch"


def evaluate_ex0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0024."""
    return run_spec_rule(EX0024ExitCloseBelowEMA20AfterTouchRule, df)
