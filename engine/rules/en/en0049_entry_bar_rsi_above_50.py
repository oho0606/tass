"""EN0049 — Entry Bar RSI Above 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0049EntryBarRSIAbove50Rule(SpecRule):
    rule_id = "EN0049"
    rule_name = "Entry Bar RSI Above 50"


def evaluate_en0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0049."""
    return run_spec_rule(EN0049EntryBarRSIAbove50Rule, df)
