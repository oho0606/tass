"""EN0053 — Entry Close Near Bar High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0053EntryCloseNearBarHighRule(SpecRule):
    rule_id = "EN0053"
    rule_name = "Entry Close Near Bar High"


def evaluate_en0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0053."""
    return run_spec_rule(EN0053EntryCloseNearBarHighRule, df)
