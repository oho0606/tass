"""VO0040 — Bollinger Band Width At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0040BollingerBandWidthAtNPeriodHighRule(SpecRule):
    rule_id = "VO0040"
    rule_name = "Bollinger Band Width At N-Period High"


def evaluate_vo0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0040."""
    return run_spec_rule(VO0040BollingerBandWidthAtNPeriodHighRule, df)
