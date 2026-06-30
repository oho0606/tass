"""GP0023 — Breakaway Gap Down Open Below N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0023BreakawayGapDownOpenBelowNPeriodLowRule(SpecRule):
    rule_id = "GP0023"
    rule_name = "Breakaway Gap Down Open Below N-Period Low"


def evaluate_gp0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0023."""
    return run_spec_rule(GP0023BreakawayGapDownOpenBelowNPeriodLowRule, df)
