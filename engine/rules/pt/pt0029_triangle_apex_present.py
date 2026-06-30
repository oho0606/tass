"""PT0029 — Triangle Apex Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0029TriangleApexPresentRule(SpecRule):
    rule_id = "PT0029"
    rule_name = "Triangle Apex Present"


def evaluate_pt0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0029."""
    return run_spec_rule(PT0029TriangleApexPresentRule, df)
