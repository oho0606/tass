"""VL0014 — Relative Volume Above 2. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0014RelativeVolumeAbove2Rule(RelativeVolumeRule):
    rule_id = "VL0014"
    rule_name = "Relative Volume Above 2"
    mode = "above_2"


def evaluate_vl0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0014."""
    return run_relative_rule(VL0014RelativeVolumeAbove2Rule, df)
