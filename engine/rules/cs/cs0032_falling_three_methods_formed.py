"""CS0032 — Falling Three Methods Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0032FallingThreeMethodsFormedRule(SpecRule):
    rule_id = "CS0032"
    rule_name = "Falling Three Methods Formed"


def evaluate_cs0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0032."""
    return run_spec_rule(CS0032FallingThreeMethodsFormedRule, df)
