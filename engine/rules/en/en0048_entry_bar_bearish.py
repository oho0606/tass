"""EN0048 — Entry Bar Bearish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0048EntryBarBearishRule(SpecRule):
    rule_id = "EN0048"
    rule_name = "Entry Bar Bearish"


def evaluate_en0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0048."""
    return run_spec_rule(EN0048EntryBarBearishRule, df)
