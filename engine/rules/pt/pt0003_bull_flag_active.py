"""PT0003 — Bull Flag Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0003BullFlagActiveRule(SpecRule):
    rule_id = "PT0003"
    rule_name = "Bull Flag Active"


def evaluate_pt0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0003."""
    return run_spec_rule(PT0003BullFlagActiveRule, df)
