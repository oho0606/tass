"""MS0041 — Bullish Change of Character. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0041BullishChangeofCharacterRule(SpecRule):
    rule_id = "MS0041"
    rule_name = "Bullish Change of Character"


def evaluate_ms0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0041."""
    return run_spec_rule(MS0041BullishChangeofCharacterRule, df)
