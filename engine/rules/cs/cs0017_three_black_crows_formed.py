"""CS0017 — Three Black Crows Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0017ThreeBlackCrowsFormedRule(SpecRule):
    rule_id = "CS0017"
    rule_name = "Three Black Crows Formed"


def evaluate_cs0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0017."""
    return run_spec_rule(CS0017ThreeBlackCrowsFormedRule, df)
