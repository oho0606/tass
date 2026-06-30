"""VL0032 — Volume Above Spike Threshold. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import SpikeThresholdRule, run_spike_rule


class VL0032VolumeAboveSpikeThresholdRule(SpikeThresholdRule):
    rule_id = "VL0032"
    rule_name = "Volume Above Spike Threshold"


def evaluate_vl0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0032."""
    return run_spike_rule(VL0032VolumeAboveSpikeThresholdRule, df)
