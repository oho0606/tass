"""VL0033 — Volume Sudden Increase. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import SuddenVolumeChangeRule, run_spike_rule


class VL0033VolumeSuddenIncreaseRule(SuddenVolumeChangeRule):
    rule_id = "VL0033"
    rule_name = "Volume Sudden Increase"
    direction = "increase"


def evaluate_vl0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0033."""
    return run_spike_rule(VL0033VolumeSuddenIncreaseRule, df)
