"""VL0007 — Volume Above N-Period High. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0007VolumeAboveNPeriodHighRule(AbsoluteVolumeRule):
    rule_id = "VL0007"
    rule_name = "Volume Above N-Period High"
    mode = "above_high"


def evaluate_vl0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0007."""
    return run_absolute_rule(VL0007VolumeAboveNPeriodHighRule, df)
