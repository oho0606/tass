"""PT0030 — Triangle Boundaries Converging. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0030TriangleBoundariesConvergingRule(SpecRule):
    rule_id = "PT0030"
    rule_name = "Triangle Boundaries Converging"


def evaluate_pt0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0030."""
    return run_spec_rule(PT0030TriangleBoundariesConvergingRule, df)
