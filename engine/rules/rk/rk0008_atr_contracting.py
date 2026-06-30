"""RK0008 — ATR Contracting. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0008ATRContractingRule(SpecRule):
    rule_id = "RK0008"
    rule_name = "ATR Contracting"


def evaluate_rk0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0008."""
    return run_spec_rule(RK0008ATRContractingRule, df)
