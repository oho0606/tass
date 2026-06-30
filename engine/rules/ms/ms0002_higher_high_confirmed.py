"""MS0002 — Higher High Confirmed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0002HigherHighConfirmedRule(SpecRule):
    rule_id = "MS0002"
    rule_name = "Higher High Confirmed"


def evaluate_ms0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0002."""
    return run_spec_rule(MS0002HigherHighConfirmedRule, df)
