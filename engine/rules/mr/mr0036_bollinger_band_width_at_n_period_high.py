"""MR0036 — Bollinger Band Width At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0036BollingerBandWidthAtNPeriodHighRule(SpecRule):
    rule_id = "MR0036"
    rule_name = "Bollinger Band Width At N-Period High"


def evaluate_mr0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0036."""
    return run_spec_rule(MR0036BollingerBandWidthAtNPeriodHighRule, df)
