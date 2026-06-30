"""MO0047 — MFI Cross Above 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0047MFICrossAbove50Rule(SpecRule):
    rule_id = "MO0047"
    rule_name = "MFI Cross Above 50"


def evaluate_mo0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0047."""
    return run_spec_rule(MO0047MFICrossAbove50Rule, df)
