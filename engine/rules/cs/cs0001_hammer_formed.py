"""CS0001 — Hammer Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0001HammerFormedRule(SpecRule):
    rule_id = "CS0001"
    rule_name = "Hammer Formed"


def evaluate_cs0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0001."""
    return run_spec_rule(CS0001HammerFormedRule, df)
