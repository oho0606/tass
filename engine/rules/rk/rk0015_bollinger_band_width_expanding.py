"""RK0015 — Bollinger Band Width Expanding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0015BollingerBandWidthExpandingRule(SpecRule):
    rule_id = "RK0015"
    rule_name = "Bollinger Band Width Expanding"


def evaluate_rk0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0015."""
    return run_spec_rule(RK0015BollingerBandWidthExpandingRule, df)
