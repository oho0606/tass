"""CS0011 — Hanging Man Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0011HangingManFormedRule(SpecRule):
    rule_id = "CS0011"
    rule_name = "Hanging Man Formed"


def evaluate_cs0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0011."""
    return run_spec_rule(CS0011HangingManFormedRule, df)
