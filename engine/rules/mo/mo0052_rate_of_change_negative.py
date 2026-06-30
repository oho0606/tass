"""MO0052 — Rate of Change Negative. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0052RateofChangeNegativeRule(SpecRule):
    rule_id = "MO0052"
    rule_name = "Rate of Change Negative"


def evaluate_mo0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0052."""
    return run_spec_rule(MO0052RateofChangeNegativeRule, df)
