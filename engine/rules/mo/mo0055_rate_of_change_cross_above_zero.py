"""MO0055 — Rate of Change Cross Above Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0055RateofChangeCrossAboveZeroRule(SpecRule):
    rule_id = "MO0055"
    rule_name = "Rate of Change Cross Above Zero"


def evaluate_mo0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0055."""
    return run_spec_rule(MO0055RateofChangeCrossAboveZeroRule, df)
