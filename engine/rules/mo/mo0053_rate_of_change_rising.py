"""MO0053 — Rate of Change Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0053RateofChangeRisingRule(SpecRule):
    rule_id = "MO0053"
    rule_name = "Rate of Change Rising"


def evaluate_mo0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0053."""
    return run_spec_rule(MO0053RateofChangeRisingRule, df)
