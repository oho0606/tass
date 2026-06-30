"""PT0007 — Bull Pennant Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0007BullPennantActiveRule(SpecRule):
    rule_id = "PT0007"
    rule_name = "Bull Pennant Active"


def evaluate_pt0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0007."""
    return run_spec_rule(PT0007BullPennantActiveRule, df)
