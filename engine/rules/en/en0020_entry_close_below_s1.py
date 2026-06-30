"""EN0020 — Entry Close Below S1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0020EntryCloseBelowS1Rule(SpecRule):
    rule_id = "EN0020"
    rule_name = "Entry Close Below S1"


def evaluate_en0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0020."""
    return run_spec_rule(EN0020EntryCloseBelowS1Rule, df)
