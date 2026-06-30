"""VL0041 — Up Bar Volume Above Average. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import BarVolumeRule, run_confirmation_rule


class VL0041UpBarVolumeAboveAverageRule(BarVolumeRule):
    rule_id = "VL0041"
    rule_name = "Up Bar Volume Above Average"
    mode = "up_above_avg"


def evaluate_vl0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0041."""
    return run_confirmation_rule(VL0041UpBarVolumeAboveAverageRule, df)
