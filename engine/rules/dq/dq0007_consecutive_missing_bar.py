"""DQ0007 — Consecutive Missing Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0007ConsecutiveMissingBarRule(SpecRule):
    rule_id = "DQ0007"
    rule_name = "Consecutive Missing Bar"


def evaluate_dq0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0007."""
    return run_spec_rule(DQ0007ConsecutiveMissingBarRule, df)
