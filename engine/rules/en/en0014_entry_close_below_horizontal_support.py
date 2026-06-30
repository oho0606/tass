"""EN0014 — Entry Close Below Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0014EntryCloseBelowHorizontalSupportRule(SpecRule):
    rule_id = "EN0014"
    rule_name = "Entry Close Below Horizontal Support"


def evaluate_en0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0014."""
    return run_spec_rule(EN0014EntryCloseBelowHorizontalSupportRule, df)
