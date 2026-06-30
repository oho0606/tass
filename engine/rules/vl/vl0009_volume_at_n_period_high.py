"""VL0009 — Volume At N-Period High. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0009VolumeAtNPeriodHighRule(AbsoluteVolumeRule):
    rule_id = "VL0009"
    rule_name = "Volume At N-Period High"
    mode = "at_high"


def evaluate_vl0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0009."""
    return run_absolute_rule(VL0009VolumeAtNPeriodHighRule, df)
