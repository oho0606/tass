"""DQ0037 — Low Liquidity Session. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0037LowLiquiditySessionRule(SpecRule):
    rule_id = "DQ0037"
    rule_name = "Low Liquidity Session"


def evaluate_dq0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0037."""
    return run_spec_rule(DQ0037LowLiquiditySessionRule, df)
