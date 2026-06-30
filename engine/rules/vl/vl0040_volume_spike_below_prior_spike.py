"""VL0040 — Volume Spike Below Prior Spike. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import SpikeCompareRule, run_spike_rule


class VL0040VolumeSpikeBelowPriorSpikeRule(SpikeCompareRule):
    rule_id = "VL0040"
    rule_name = "Volume Spike Below Prior Spike"
    comparison = "below_prior"


def evaluate_vl0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0040."""
    return run_spike_rule(VL0040VolumeSpikeBelowPriorSpikeRule, df)
