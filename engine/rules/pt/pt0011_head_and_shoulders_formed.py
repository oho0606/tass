"""PT0011 — Head And Shoulders Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0011HeadAndShouldersFormedRule(SpecRule):
    rule_id = "PT0011"
    rule_name = "Head And Shoulders Formed"


def evaluate_pt0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0011."""
    return run_spec_rule(PT0011HeadAndShouldersFormedRule, df)
