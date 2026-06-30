"""GP0024 — Breakaway Gap Down High Below N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0024BreakawayGapDownHighBelowNPeriodLowRule(SpecRule):
    rule_id = "GP0024"
    rule_name = "Breakaway Gap Down High Below N-Period Low"


def evaluate_gp0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0024."""
    return run_spec_rule(GP0024BreakawayGapDownHighBelowNPeriodLowRule, df)
