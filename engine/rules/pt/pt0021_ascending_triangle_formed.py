"""PT0021 — Ascending Triangle Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0021AscendingTriangleFormedRule(SpecRule):
    rule_id = "PT0021"
    rule_name = "Ascending Triangle Formed"


def evaluate_pt0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0021."""
    return run_spec_rule(PT0021AscendingTriangleFormedRule, df)
