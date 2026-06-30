"""MO0046 — MFI Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0046MFIFallingRule(SpecRule):
    rule_id = "MO0046"
    rule_name = "MFI Falling"


def evaluate_mo0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0046."""
    return run_spec_rule(MO0046MFIFallingRule, df)
