"""RK0055 — Volatility Extended Above 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0055VolatilityExtendedAbove20PeriodAverageRule(SpecRule):
    rule_id = "RK0055"
    rule_name = "Volatility Extended Above 20-Period Average"


def evaluate_rk0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0055."""
    return run_spec_rule(RK0055VolatilityExtendedAbove20PeriodAverageRule, df)
