"""MO0005 — RSI Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0005RSIRisingRule(SpecRule):
    rule_id = "MO0005"
    rule_name = "RSI Rising"


def evaluate_mo0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0005."""
    return run_spec_rule(MO0005RSIRisingRule, df)
