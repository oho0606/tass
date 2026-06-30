"""MO0041 — MFI Above 80. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0041MFIAbove80Rule(SpecRule):
    rule_id = "MO0041"
    rule_name = "MFI Above 80"


def evaluate_mo0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0041."""
    return run_spec_rule(MO0041MFIAbove80Rule, df)
