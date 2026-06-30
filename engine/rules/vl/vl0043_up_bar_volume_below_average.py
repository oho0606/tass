"""VL0043 — Up Bar Volume Below Average. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import BarVolumeRule, run_confirmation_rule


class VL0043UpBarVolumeBelowAverageRule(BarVolumeRule):
    rule_id = "VL0043"
    rule_name = "Up Bar Volume Below Average"
    mode = "up_below_avg"


def evaluate_vl0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0043."""
    return run_confirmation_rule(VL0043UpBarVolumeBelowAverageRule, df)
