"""MS0042 — Bearish Change of Character. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0042BearishChangeofCharacterRule(SpecRule):
    rule_id = "MS0042"
    rule_name = "Bearish Change of Character"


def evaluate_ms0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0042."""
    return run_spec_rule(MS0042BearishChangeofCharacterRule, df)
