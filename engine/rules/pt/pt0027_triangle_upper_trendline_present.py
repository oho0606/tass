"""PT0027 — Triangle Upper Trendline Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0027TriangleUpperTrendlinePresentRule(SpecRule):
    rule_id = "PT0027"
    rule_name = "Triangle Upper Trendline Present"


def evaluate_pt0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0027."""
    return run_spec_rule(PT0027TriangleUpperTrendlinePresentRule, df)
