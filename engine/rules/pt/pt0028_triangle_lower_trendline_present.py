"""PT0028 — Triangle Lower Trendline Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0028TriangleLowerTrendlinePresentRule(SpecRule):
    rule_id = "PT0028"
    rule_name = "Triangle Lower Trendline Present"


def evaluate_pt0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0028."""
    return run_spec_rule(PT0028TriangleLowerTrendlinePresentRule, df)
