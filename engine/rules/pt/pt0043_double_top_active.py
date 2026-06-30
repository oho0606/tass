"""PT0043 — Double Top Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0043DoubleTopActiveRule(SpecRule):
    rule_id = "PT0043"
    rule_name = "Double Top Active"


def evaluate_pt0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0043."""
    return run_spec_rule(PT0043DoubleTopActiveRule, df)
