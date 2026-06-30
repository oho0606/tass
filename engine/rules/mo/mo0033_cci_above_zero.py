"""MO0033 — CCI Above Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0033CCIAboveZeroRule(SpecRule):
    rule_id = "MO0033"
    rule_name = "CCI Above Zero"


def evaluate_mo0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0033."""
    return run_spec_rule(MO0033CCIAboveZeroRule, df)
