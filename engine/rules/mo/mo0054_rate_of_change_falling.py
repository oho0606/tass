"""MO0054 — Rate of Change Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0054RateofChangeFallingRule(SpecRule):
    rule_id = "MO0054"
    rule_name = "Rate of Change Falling"


def evaluate_mo0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0054."""
    return run_spec_rule(MO0054RateofChangeFallingRule, df)
