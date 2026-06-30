"""VL0059 — Volume Structure Stable. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import VolumeStructureStableRule, run_quality_rule


class VL0059VolumeStructureStableRule(VolumeStructureStableRule):
    rule_id = "VL0059"
    rule_name = "Volume Structure Stable"


def evaluate_vl0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0059."""
    return run_quality_rule(VL0059VolumeStructureStableRule, df)
