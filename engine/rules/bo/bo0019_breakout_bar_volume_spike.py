"""BO0019 — Breakout Bar Volume Spike. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0019BreakoutBarVolumeSpikeRule(SpecRule):
    rule_id = "BO0019"
    rule_name = "Breakout Bar Volume Spike"


def evaluate_bo0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0019."""
    return run_spec_rule(BO0019BreakoutBarVolumeSpikeRule, df)
