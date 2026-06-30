"""GP0010 — Consecutive Gap Up Day. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0010ConsecutiveGapUpDayRule(SpecRule):
    rule_id = "GP0010"
    rule_name = "Consecutive Gap Up Day"


def evaluate_gp0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0010."""
    return run_spec_rule(GP0010ConsecutiveGapUpDayRule, df)
