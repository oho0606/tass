"""VL0013 — Relative Volume Equal 1. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0013RelativeVolumeEqual1Rule(RelativeVolumeRule):
    rule_id = "VL0013"
    rule_name = "Relative Volume Equal 1"
    mode = "equal_1"


def evaluate_vl0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0013."""
    return run_relative_rule(VL0013RelativeVolumeEqual1Rule, df)
