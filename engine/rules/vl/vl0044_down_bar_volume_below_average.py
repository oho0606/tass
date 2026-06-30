"""VL0044 — Down Bar Volume Below Average. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import BarVolumeRule, run_confirmation_rule


class VL0044DownBarVolumeBelowAverageRule(BarVolumeRule):
    rule_id = "VL0044"
    rule_name = "Down Bar Volume Below Average"
    mode = "down_below_avg"


def evaluate_vl0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0044."""
    return run_confirmation_rule(VL0044DownBarVolumeBelowAverageRule, df)
