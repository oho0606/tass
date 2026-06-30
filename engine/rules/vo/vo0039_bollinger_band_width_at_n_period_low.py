"""VO0039 — Bollinger Band Width At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0039BollingerBandWidthAtNPeriodLowRule(SpecRule):
    rule_id = "VO0039"
    rule_name = "Bollinger Band Width At N-Period Low"


def evaluate_vo0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0039."""
    return run_spec_rule(VO0039BollingerBandWidthAtNPeriodLowRule, df)
