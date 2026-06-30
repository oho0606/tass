"""GP0025 — Breakaway Gap Up Open Outside N-Period Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0025BreakawayGapUpOpenOutsideNPeriodRangeRule(SpecRule):
    rule_id = "GP0025"
    rule_name = "Breakaway Gap Up Open Outside N-Period Range"


def evaluate_gp0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0025."""
    return run_spec_rule(GP0025BreakawayGapUpOpenOutsideNPeriodRangeRule, df)
