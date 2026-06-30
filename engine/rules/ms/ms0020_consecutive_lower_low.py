"""MS0020 — Consecutive Lower Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0020ConsecutiveLowerLowRule(SpecRule):
    rule_id = "MS0020"
    rule_name = "Consecutive Lower Low"


def evaluate_ms0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0020."""
    return run_spec_rule(MS0020ConsecutiveLowerLowRule, df)
