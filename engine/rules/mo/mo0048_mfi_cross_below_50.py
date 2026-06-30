"""MO0048 — MFI Cross Below 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0048MFICrossBelow50Rule(SpecRule):
    rule_id = "MO0048"
    rule_name = "MFI Cross Below 50"


def evaluate_mo0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0048."""
    return run_spec_rule(MO0048MFICrossBelow50Rule, df)
