"""MO0056 — Rate of Change Cross Below Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0056RateofChangeCrossBelowZeroRule(SpecRule):
    rule_id = "MO0056"
    rule_name = "Rate of Change Cross Below Zero"


def evaluate_mo0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0056."""
    return run_spec_rule(MO0056RateofChangeCrossBelowZeroRule, df)
