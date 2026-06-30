"""EX0007 — Exit Close Below Prior Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0007ExitCloseBelowPriorCloseRule(SpecRule):
    rule_id = "EX0007"
    rule_name = "Exit Close Below Prior Close"


def evaluate_ex0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0007."""
    return run_spec_rule(EX0007ExitCloseBelowPriorCloseRule, df)
