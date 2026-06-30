"""MR0046 — Bollinger Band Width At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0046BollingerBandWidthAtNPeriodLowRule(SpecRule):
    rule_id = "MR0046"
    rule_name = "Bollinger Band Width At N-Period Low"


def evaluate_mr0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0046."""
    return run_spec_rule(MR0046BollingerBandWidthAtNPeriodLowRule, df)
