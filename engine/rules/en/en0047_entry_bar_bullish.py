"""EN0047 — Entry Bar Bullish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0047EntryBarBullishRule(SpecRule):
    rule_id = "EN0047"
    rule_name = "Entry Bar Bullish"


def evaluate_en0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0047."""
    return run_spec_rule(EN0047EntryBarBullishRule, df)
