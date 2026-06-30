"""MR0010 — Close At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0010CloseAtNPeriodHighRule(SpecRule):
    rule_id = "MR0010"
    rule_name = "Close At N-Period High"


def evaluate_mr0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0010."""
    return run_spec_rule(MR0010CloseAtNPeriodHighRule, df)
