"""RK0021 — Overnight Gap Up Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0021OvernightGapUpPresentRule(SpecRule):
    rule_id = "RK0021"
    rule_name = "Overnight Gap Up Present"


def evaluate_rk0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0021."""
    return run_spec_rule(RK0021OvernightGapUpPresentRule, df)
