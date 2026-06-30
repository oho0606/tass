"""VL0021 — Volume Rising. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import VolumeDirectionRule, run_trend_rule


class VL0021VolumeRisingRule(VolumeDirectionRule):
    rule_id = "VL0021"
    rule_name = "Volume Rising"
    direction = "rising"


def evaluate_vl0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0021."""
    return run_trend_rule(VL0021VolumeRisingRule, df)
