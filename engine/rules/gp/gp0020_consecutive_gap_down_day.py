"""GP0020 — Consecutive Gap Down Day. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0020ConsecutiveGapDownDayRule(SpecRule):
    rule_id = "GP0020"
    rule_name = "Consecutive Gap Down Day"


def evaluate_gp0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0020."""
    return run_spec_rule(GP0020ConsecutiveGapDownDayRule, df)
