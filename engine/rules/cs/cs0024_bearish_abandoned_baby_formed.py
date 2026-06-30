"""CS0024 — Bearish Abandoned Baby Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0024BearishAbandonedBabyFormedRule(SpecRule):
    rule_id = "CS0024"
    rule_name = "Bearish Abandoned Baby Formed"


def evaluate_cs0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0024."""
    return run_spec_rule(CS0024BearishAbandonedBabyFormedRule, df)
