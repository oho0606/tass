"""BO0014 — Breakout Bar Volume Below Prior Volume. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0014BreakoutBarVolumeBelowPriorVolumeRule(SpecRule):
    rule_id = "BO0014"
    rule_name = "Breakout Bar Volume Below Prior Volume"


def evaluate_bo0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0014."""
    return run_spec_rule(BO0014BreakoutBarVolumeBelowPriorVolumeRule, df)
