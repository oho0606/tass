"""CS0025 — Island Reversal Bottom Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0025IslandReversalBottomFormedRule(SpecRule):
    rule_id = "CS0025"
    rule_name = "Island Reversal Bottom Formed"


def evaluate_cs0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0025."""
    return run_spec_rule(CS0025IslandReversalBottomFormedRule, df)
