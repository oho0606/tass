"""VL0039 — Volume Spike Above Prior Spike. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import SpikeCompareRule, run_spike_rule


class VL0039VolumeSpikeAbovePriorSpikeRule(SpikeCompareRule):
    rule_id = "VL0039"
    rule_name = "Volume Spike Above Prior Spike"
    comparison = "above_prior"


def evaluate_vl0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0039."""
    return run_spike_rule(VL0039VolumeSpikeAbovePriorSpikeRule, df)
