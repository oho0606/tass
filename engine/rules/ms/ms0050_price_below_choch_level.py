"""MS0050 — Price Below CHoCH Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0050PriceBelowCHoCHLevelRule(SpecRule):
    rule_id = "MS0050"
    rule_name = "Price Below CHoCH Level"


def evaluate_ms0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0050."""
    return run_spec_rule(MS0050PriceBelowCHoCHLevelRule, df)
