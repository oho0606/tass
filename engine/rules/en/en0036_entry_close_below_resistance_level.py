"""EN0036 — Entry Close Below Resistance Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0036EntryCloseBelowResistanceLevelRule(SpecRule):
    rule_id = "EN0036"
    rule_name = "Entry Close Below Resistance Level"


def evaluate_en0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0036."""
    return run_spec_rule(EN0036EntryCloseBelowResistanceLevelRule, df)
