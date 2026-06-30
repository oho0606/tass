"""VL0035 — Volume Expansion. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import VolumeSpreadTrendRule, run_spike_rule


class VL0035VolumeExpansionRule(VolumeSpreadTrendRule):
    rule_id = "VL0035"
    rule_name = "Volume Expansion"
    trend = "expansion"


def evaluate_vl0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0035."""
    return run_spike_rule(VL0035VolumeExpansionRule, df)
