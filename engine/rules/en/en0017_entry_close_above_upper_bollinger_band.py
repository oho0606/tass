"""EN0017 — Entry Close Above Upper Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0017EntryCloseAboveUpperBollingerBandRule(SpecRule):
    rule_id = "EN0017"
    rule_name = "Entry Close Above Upper Bollinger Band"


def evaluate_en0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0017."""
    return run_spec_rule(EN0017EntryCloseAboveUpperBollingerBandRule, df)
