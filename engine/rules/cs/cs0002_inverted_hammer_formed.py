"""CS0002 — Inverted Hammer Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0002InvertedHammerFormedRule(SpecRule):
    rule_id = "CS0002"
    rule_name = "Inverted Hammer Formed"


def evaluate_cs0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0002."""
    return run_spec_rule(CS0002InvertedHammerFormedRule, df)
