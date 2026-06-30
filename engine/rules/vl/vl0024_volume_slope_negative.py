"""VL0024 — Volume Slope Negative. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import VolumeDirectionRule, run_trend_rule


class VL0024VolumeSlopeNegativeRule(VolumeDirectionRule):
    rule_id = "VL0024"
    rule_name = "Volume Slope Negative"
    direction = "falling"


def evaluate_vl0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0024."""
    return run_trend_rule(VL0024VolumeSlopeNegativeRule, df)
