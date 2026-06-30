"""EN0019 — Entry Close Above R1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0019EntryCloseAboveR1Rule(SpecRule):
    rule_id = "EN0019"
    rule_name = "Entry Close Above R1"


def evaluate_en0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0019."""
    return run_spec_rule(EN0019EntryCloseAboveR1Rule, df)
