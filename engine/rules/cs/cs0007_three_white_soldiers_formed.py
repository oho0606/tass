"""CS0007 — Three White Soldiers Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0007ThreeWhiteSoldiersFormedRule(SpecRule):
    rule_id = "CS0007"
    rule_name = "Three White Soldiers Formed"


def evaluate_cs0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0007."""
    return run_spec_rule(CS0007ThreeWhiteSoldiersFormedRule, df)
