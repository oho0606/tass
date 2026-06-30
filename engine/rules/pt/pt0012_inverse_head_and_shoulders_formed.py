"""PT0012 — Inverse Head And Shoulders Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0012InverseHeadAndShouldersFormedRule(SpecRule):
    rule_id = "PT0012"
    rule_name = "Inverse Head And Shoulders Formed"


def evaluate_pt0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0012."""
    return run_spec_rule(PT0012InverseHeadAndShouldersFormedRule, df)
