"""MO0043 — MFI Above 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0043MFIAbove50Rule(SpecRule):
    rule_id = "MO0043"
    rule_name = "MFI Above 50"


def evaluate_mo0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0043."""
    return run_spec_rule(MO0043MFIAbove50Rule, df)
