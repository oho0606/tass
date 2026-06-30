"""VL0037 — Volume Climax. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import VolumeClimaxRule, run_spike_rule


class VL0037VolumeClimaxRule(VolumeClimaxRule):
    rule_id = "VL0037"
    rule_name = "Volume Climax"


def evaluate_vl0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0037."""
    return run_spike_rule(VL0037VolumeClimaxRule, df)
