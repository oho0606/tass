"""VL0060 — Volume Pattern Consistent. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import VolumePatternConsistentRule, run_quality_rule


class VL0060VolumePatternConsistentRule(VolumePatternConsistentRule):
    rule_id = "VL0060"
    rule_name = "Volume Pattern Consistent"


def evaluate_vl0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0060."""
    return run_quality_rule(VL0060VolumePatternConsistentRule, df)
