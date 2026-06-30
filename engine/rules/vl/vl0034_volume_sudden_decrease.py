"""VL0034 — Volume Sudden Decrease. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import SuddenVolumeChangeRule, run_spike_rule


class VL0034VolumeSuddenDecreaseRule(SuddenVolumeChangeRule):
    rule_id = "VL0034"
    rule_name = "Volume Sudden Decrease"
    direction = "decrease"


def evaluate_vl0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0034."""
    return run_spike_rule(VL0034VolumeSuddenDecreaseRule, df)
