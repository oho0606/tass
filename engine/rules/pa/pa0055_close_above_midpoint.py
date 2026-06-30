"""PA0055 — Close Above Midpoint. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0055CloseAboveMidpointRule(SpecRule):
    rule_id = "PA0055"
    rule_name = "Close Above Midpoint"


def evaluate_pa0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0055."""
    return run_spec_rule(PA0055CloseAboveMidpointRule, df)
