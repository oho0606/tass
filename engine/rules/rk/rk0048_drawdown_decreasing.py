"""RK0048 — Drawdown Decreasing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0048DrawdownDecreasingRule(SpecRule):
    rule_id = "RK0048"
    rule_name = "Drawdown Decreasing"


def evaluate_rk0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0048."""
    return run_spec_rule(RK0048DrawdownDecreasingRule, df)
