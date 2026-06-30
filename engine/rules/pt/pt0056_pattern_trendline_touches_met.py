"""PT0056 — Pattern Trendline Touches Met. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0056PatternTrendlineTouchesMetRule(SpecRule):
    rule_id = "PT0056"
    rule_name = "Pattern Trendline Touches Met"


def evaluate_pt0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0056."""
    return run_spec_rule(PT0056PatternTrendlineTouchesMetRule, df)
