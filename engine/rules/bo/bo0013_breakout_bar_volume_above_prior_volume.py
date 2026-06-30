"""BO0013 — Breakout Bar Volume Above Prior Volume. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0013BreakoutBarVolumeAbovePriorVolumeRule(SpecRule):
    rule_id = "BO0013"
    rule_name = "Breakout Bar Volume Above Prior Volume"


def evaluate_bo0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0013."""
    return run_spec_rule(BO0013BreakoutBarVolumeAbovePriorVolumeRule, df)
