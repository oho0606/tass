"""MR0025 — N-Period Return Near Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0025NPeriodReturnNearZeroRule(SpecRule):
    rule_id = "MR0025"
    rule_name = "N-Period Return Near Zero"


def evaluate_mr0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0025."""
    return run_spec_rule(MR0025NPeriodReturnNearZeroRule, df)
