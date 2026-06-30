"""RK0058 — Drawdown Near 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0058DrawdownNear20PeriodAverageRule(SpecRule):
    rule_id = "RK0058"
    rule_name = "Drawdown Near 20-Period Average"


def evaluate_rk0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0058."""
    return run_spec_rule(RK0058DrawdownNear20PeriodAverageRule, df)
