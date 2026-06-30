"""DQ0011 — High Below Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0011HighBelowLowRule(SpecRule):
    rule_id = "DQ0011"
    rule_name = "High Below Low"


def evaluate_dq0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0011."""
    return run_spec_rule(DQ0011HighBelowLowRule, df)
