"""VL0005 — Volume Below Prior Volume. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0005VolumeBelowPriorVolumeRule(AbsoluteVolumeRule):
    rule_id = "VL0005"
    rule_name = "Volume Below Prior Volume"
    mode = "below_prior"


def evaluate_vl0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0005."""
    return run_absolute_rule(VL0005VolumeBelowPriorVolumeRule, df)
