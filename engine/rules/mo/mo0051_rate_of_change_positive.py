"""MO0051 — Rate of Change Positive. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0051RateofChangePositiveRule(SpecRule):
    rule_id = "MO0051"
    rule_name = "Rate of Change Positive"


def evaluate_mo0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0051."""
    return run_spec_rule(MO0051RateofChangePositiveRule, df)
