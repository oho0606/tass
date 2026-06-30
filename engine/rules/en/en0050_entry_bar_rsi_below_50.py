"""EN0050 — Entry Bar RSI Below 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0050EntryBarRSIBelow50Rule(SpecRule):
    rule_id = "EN0050"
    rule_name = "Entry Bar RSI Below 50"


def evaluate_en0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0050."""
    return run_spec_rule(EN0050EntryBarRSIBelow50Rule, df)
