"""RK0022 — Overnight Gap Down Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0022OvernightGapDownPresentRule(SpecRule):
    rule_id = "RK0022"
    rule_name = "Overnight Gap Down Present"


def evaluate_rk0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0022."""
    return run_spec_rule(RK0022OvernightGapDownPresentRule, df)
