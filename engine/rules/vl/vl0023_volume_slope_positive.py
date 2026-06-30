"""VL0023 — Volume Slope Positive. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import VolumeDirectionRule, run_trend_rule


class VL0023VolumeSlopePositiveRule(VolumeDirectionRule):
    rule_id = "VL0023"
    rule_name = "Volume Slope Positive"
    direction = "rising"


def evaluate_vl0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0023."""
    return run_trend_rule(VL0023VolumeSlopePositiveRule, df)
