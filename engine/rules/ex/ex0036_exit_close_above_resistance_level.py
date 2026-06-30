"""EX0036 — Exit Close Above Resistance Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0036ExitCloseAboveResistanceLevelRule(SpecRule):
    rule_id = "EX0036"
    rule_name = "Exit Close Above Resistance Level"


def evaluate_ex0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0036."""
    return run_spec_rule(EX0036ExitCloseAboveResistanceLevelRule, df)
