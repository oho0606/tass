"""RK0025 — Unfilled Gap Up Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0025UnfilledGapUpPresentRule(SpecRule):
    rule_id = "RK0025"
    rule_name = "Unfilled Gap Up Present"


def evaluate_rk0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0025."""
    return run_spec_rule(RK0025UnfilledGapUpPresentRule, df)
