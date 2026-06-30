"""GP0030 — Breakaway Gap Down Volume Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0030BreakawayGapDownVolumeAboveNPeriodAverageRule(SpecRule):
    rule_id = "GP0030"
    rule_name = "Breakaway Gap Down Volume Above N-Period Average"


def evaluate_gp0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0030."""
    return run_spec_rule(GP0030BreakawayGapDownVolumeAboveNPeriodAverageRule, df)
