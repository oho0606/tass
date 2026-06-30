"""EX0033 — Exit Low At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0033ExitLowAtNPeriodLowRule(SpecRule):
    rule_id = "EX0033"
    rule_name = "Exit Low At N-Period Low"


def evaluate_ex0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0033."""
    return run_spec_rule(EX0033ExitLowAtNPeriodLowRule, df)
