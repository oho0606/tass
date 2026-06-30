"""MS0049 — Price Above CHoCH Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0049PriceAboveCHoCHLevelRule(SpecRule):
    rule_id = "MS0049"
    rule_name = "Price Above CHoCH Level"


def evaluate_ms0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0049."""
    return run_spec_rule(MS0049PriceAboveCHoCHLevelRule, df)
