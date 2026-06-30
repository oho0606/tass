"""CS0014 — Bearish Engulfing Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0014BearishEngulfingFormedRule(SpecRule):
    rule_id = "CS0014"
    rule_name = "Bearish Engulfing Formed"


def evaluate_cs0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0014."""
    return run_spec_rule(CS0014BearishEngulfingFormedRule, df)
