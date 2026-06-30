"""VL0031 — Volume Spike. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import VolumeSpikeRule, run_spike_rule


class VL0031VolumeSpikeRule(VolumeSpikeRule):
    rule_id = "VL0031"
    rule_name = "Volume Spike"


def evaluate_vl0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0031."""
    return run_spike_rule(VL0031VolumeSpikeRule, df)
