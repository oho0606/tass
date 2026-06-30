"""MR0049 — Volatility Below Prior Period. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0049VolatilityBelowPriorPeriodRule(SpecRule):
    rule_id = "MR0049"
    rule_name = "Volatility Below Prior Period"


def evaluate_mr0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0049."""
    return run_spec_rule(MR0049VolatilityBelowPriorPeriodRule, df)
