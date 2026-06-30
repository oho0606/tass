"""EX0049 — Exit Bar RSI Below 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0049ExitBarRSIBelow50Rule(SpecRule):
    rule_id = "EX0049"
    rule_name = "Exit Bar RSI Below 50"


def evaluate_ex0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0049."""
    return run_spec_rule(EX0049ExitBarRSIBelow50Rule, df)
