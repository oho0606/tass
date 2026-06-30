"""VL0042 — Down Bar Volume Above Average. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import BarVolumeRule, run_confirmation_rule


class VL0042DownBarVolumeAboveAverageRule(BarVolumeRule):
    rule_id = "VL0042"
    rule_name = "Down Bar Volume Above Average"
    mode = "down_above_avg"


def evaluate_vl0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0042."""
    return run_confirmation_rule(VL0042DownBarVolumeAboveAverageRule, df)
