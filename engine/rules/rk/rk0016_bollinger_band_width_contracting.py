"""RK0016 — Bollinger Band Width Contracting. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0016BollingerBandWidthContractingRule(SpecRule):
    rule_id = "RK0016"
    rule_name = "Bollinger Band Width Contracting"


def evaluate_rk0016(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0016."""
    return run_spec_rule(RK0016BollingerBandWidthContractingRule, df)
