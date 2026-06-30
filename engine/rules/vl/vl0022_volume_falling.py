"""VL0022 — Volume Falling. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import VolumeDirectionRule, run_trend_rule


class VL0022VolumeFallingRule(VolumeDirectionRule):
    rule_id = "VL0022"
    rule_name = "Volume Falling"
    direction = "falling"


def evaluate_vl0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0022."""
    return run_trend_rule(VL0022VolumeFallingRule, df)
