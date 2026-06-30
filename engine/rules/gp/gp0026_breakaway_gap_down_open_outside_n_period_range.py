"""GP0026 — Breakaway Gap Down Open Outside N-Period Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0026BreakawayGapDownOpenOutsideNPeriodRangeRule(SpecRule):
    rule_id = "GP0026"
    rule_name = "Breakaway Gap Down Open Outside N-Period Range"


def evaluate_gp0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0026."""
    return run_spec_rule(GP0026BreakawayGapDownOpenOutsideNPeriodRangeRule, df)
