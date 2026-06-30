"""DQ0034 — No Trade Session. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0034NoTradeSessionRule(SpecRule):
    rule_id = "DQ0034"
    rule_name = "No Trade Session"


def evaluate_dq0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0034."""
    return run_spec_rule(DQ0034NoTradeSessionRule, df)
