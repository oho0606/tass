"""VL0016 — Relative Volume Below Threshold. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0016RelativeVolumeBelowThresholdRule(RelativeVolumeRule):
    rule_id = "VL0016"
    rule_name = "Relative Volume Below Threshold"
    mode = "below_threshold"


def evaluate_vl0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0016."""
    return run_relative_rule(VL0016RelativeVolumeBelowThresholdRule, df)
