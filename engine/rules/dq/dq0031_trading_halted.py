"""DQ0031 — Trading Halted. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0031TradingHaltedRule(SpecRule):
    rule_id = "DQ0031"
    rule_name = "Trading Halted"


def evaluate_dq0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0031."""
    return run_spec_rule(DQ0031TradingHaltedRule, df)
