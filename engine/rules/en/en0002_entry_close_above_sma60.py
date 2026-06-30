"""EN0002 — Entry Close Above SMA60. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0002EntryCloseAboveSMA60Rule(SpecRule):
    rule_id = "EN0002"
    rule_name = "Entry Close Above SMA60"


def evaluate_en0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0002."""
    return run_spec_rule(EN0002EntryCloseAboveSMA60Rule, df)
