"""CS0028 — Bearish Key Reversal Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0028BearishKeyReversalFormedRule(SpecRule):
    rule_id = "CS0028"
    rule_name = "Bearish Key Reversal Formed"


def evaluate_cs0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0028."""
    return run_spec_rule(CS0028BearishKeyReversalFormedRule, df)
