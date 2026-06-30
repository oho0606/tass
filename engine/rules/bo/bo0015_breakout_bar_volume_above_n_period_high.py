"""BO0015 — Breakout Bar Volume Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0015BreakoutBarVolumeAboveNPeriodHighRule(SpecRule):
    rule_id = "BO0015"
    rule_name = "Breakout Bar Volume Above N-Period High"


def evaluate_bo0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0015."""
    return run_spec_rule(BO0015BreakoutBarVolumeAboveNPeriodHighRule, df)
