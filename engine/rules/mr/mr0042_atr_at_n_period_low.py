"""MR0042 — ATR At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0042ATRAtNPeriodLowRule(SpecRule):
    rule_id = "MR0042"
    rule_name = "ATR At N-Period Low"


def evaluate_mr0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0042."""
    return run_spec_rule(MR0042ATRAtNPeriodLowRule, df)
