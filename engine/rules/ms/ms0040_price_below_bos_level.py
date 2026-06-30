"""MS0040 — Price Below BOS Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0040PriceBelowBOSLevelRule(SpecRule):
    rule_id = "MS0040"
    rule_name = "Price Below BOS Level"


def evaluate_ms0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0040."""
    return run_spec_rule(MS0040PriceBelowBOSLevelRule, df)
