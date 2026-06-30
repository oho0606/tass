"""MO0049 — MFI Cross Above 80. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0049MFICrossAbove80Rule(SpecRule):
    rule_id = "MO0049"
    rule_name = "MFI Cross Above 80"


def evaluate_mo0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0049."""
    return run_spec_rule(MO0049MFICrossAbove80Rule, df)
