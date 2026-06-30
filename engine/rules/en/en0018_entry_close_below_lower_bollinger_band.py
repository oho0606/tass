"""EN0018 — Entry Close Below Lower Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0018EntryCloseBelowLowerBollingerBandRule(SpecRule):
    rule_id = "EN0018"
    rule_name = "Entry Close Below Lower Bollinger Band"


def evaluate_en0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0018."""
    return run_spec_rule(EN0018EntryCloseBelowLowerBollingerBandRule, df)
