"""MO0036 — CCI Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0036CCIFallingRule(SpecRule):
    rule_id = "MO0036"
    rule_name = "CCI Falling"


def evaluate_mo0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0036."""
    return run_spec_rule(MO0036CCIFallingRule, df)
