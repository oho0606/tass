"""VL0036 — Volume Contraction. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import VolumeSpreadTrendRule, run_spike_rule


class VL0036VolumeContractionRule(VolumeSpreadTrendRule):
    rule_id = "VL0036"
    rule_name = "Volume Contraction"
    trend = "contraction"


def evaluate_vl0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0036."""
    return run_spike_rule(VL0036VolumeContractionRule, df)
