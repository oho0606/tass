"""EX0016 — Exit Close Above 52-Week Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0016ExitCloseAbove52WeekLowRule(SpecRule):
    rule_id = "EX0016"
    rule_name = "Exit Close Above 52-Week Low"


def evaluate_ex0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0016."""
    return run_spec_rule(EX0016ExitCloseAbove52WeekLowRule, df)
