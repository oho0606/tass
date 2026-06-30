"""CS0006 — Morning Star Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CS0006MorningStarFormedRule(SpecRule):
    rule_id = "CS0006"
    rule_name = "Morning Star Formed"


def evaluate_cs0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CS0006."""
    return run_spec_rule(CS0006MorningStarFormedRule, df)
