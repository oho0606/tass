"""EN0001 — Entry Close Above SMA20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0001EntryCloseAboveSMA20Rule(SpecRule):
    rule_id = "EN0001"
    rule_name = "Entry Close Above SMA20"


def evaluate_en0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0001."""
    return run_spec_rule(EN0001EntryCloseAboveSMA20Rule, df)
