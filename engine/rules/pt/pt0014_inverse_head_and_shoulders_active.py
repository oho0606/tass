"""PT0014 — Inverse Head And Shoulders Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0014InverseHeadAndShouldersActiveRule(SpecRule):
    rule_id = "PT0014"
    rule_name = "Inverse Head And Shoulders Active"


def evaluate_pt0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0014."""
    return run_spec_rule(PT0014InverseHeadAndShouldersActiveRule, df)
