"""EX0004 — Exit Close Below EMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0004ExitCloseBelowEMA60Rule(SpecRule):
    rule_id = "EX0004"
    rule_name = "Exit Close Below EMA60"


def evaluate_ex0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0004."""
    return run_spec_rule(EX0004ExitCloseBelowEMA60Rule, df)
