"""VL0045 — Up Bar Volume Above Prior Up Bar. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import PriorSameBarVolumeRule, run_confirmation_rule


class VL0045UpBarVolumeAbovePriorUpBarRule(PriorSameBarVolumeRule):
    rule_id = "VL0045"
    rule_name = "Up Bar Volume Above Prior Up Bar"
    bar_direction = "up"


def evaluate_vl0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0045."""
    return run_confirmation_rule(VL0045UpBarVolumeAbovePriorUpBarRule, df)
