"""RK0056 — Volatility Extended Below 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0056VolatilityExtendedBelow20PeriodAverageRule(SpecRule):
    rule_id = "RK0056"
    rule_name = "Volatility Extended Below 20-Period Average"


def evaluate_rk0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0056."""
    return run_spec_rule(RK0056VolatilityExtendedBelow20PeriodAverageRule, df)
