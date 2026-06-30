"""DQ0038 — Wide Bid Ask Spread. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0038WideBidAskSpreadRule(SpecRule):
    rule_id = "DQ0038"
    rule_name = "Wide Bid Ask Spread"


def evaluate_dq0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0038."""
    return run_spec_rule(DQ0038WideBidAskSpreadRule, df)
