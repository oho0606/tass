"""MR0009 — N-Period Return Positive. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0009NPeriodReturnPositiveRule(SpecRule):
    rule_id = "MR0009"
    rule_name = "N-Period Return Positive"


def evaluate_mr0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0009."""
    return run_spec_rule(MR0009NPeriodReturnPositiveRule, df)
