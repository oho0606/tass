"""MR0020 — Close At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0020CloseAtNPeriodLowRule(SpecRule):
    rule_id = "MR0020"
    rule_name = "Close At N-Period Low"


def evaluate_mr0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0020."""
    return run_spec_rule(MR0020CloseAtNPeriodLowRule, df)
