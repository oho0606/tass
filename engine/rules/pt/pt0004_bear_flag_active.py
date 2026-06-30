"""PT0004 — Bear Flag Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0004BearFlagActiveRule(SpecRule):
    rule_id = "PT0004"
    rule_name = "Bear Flag Active"


def evaluate_pt0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0004."""
    return run_spec_rule(PT0004BearFlagActiveRule, df)
