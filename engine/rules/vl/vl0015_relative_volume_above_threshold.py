"""VL0015 — Relative Volume Above Threshold. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0015RelativeVolumeAboveThresholdRule(RelativeVolumeRule):
    rule_id = "VL0015"
    rule_name = "Relative Volume Above Threshold"
    mode = "above_threshold"


def evaluate_vl0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0015."""
    return run_relative_rule(VL0015RelativeVolumeAboveThresholdRule, df)
