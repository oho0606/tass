"""VL0038 — Volume Dry Up. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._spike import VolumeDryUpRule, run_spike_rule


class VL0038VolumeDryUpRule(VolumeDryUpRule):
    rule_id = "VL0038"
    rule_name = "Volume Dry Up"


def evaluate_vl0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0038."""
    return run_spike_rule(VL0038VolumeDryUpRule, df)
