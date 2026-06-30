"""CS0040 — Bearish Separating Lines Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0040BearishSeparatingLinesFormedRule(SpecRule):
    rule_id = "CS0040"
    rule_name = "Bearish Separating Lines Formed"


def evaluate_cs0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0040."""
    return run_spec_rule(CS0040BearishSeparatingLinesFormedRule, df)
