"""VO0045 — Bollinger Band Width Expanding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0045BollingerBandWidthExpandingRule(SpecRule):
    rule_id = "VO0045"
    rule_name = "Bollinger Band Width Expanding"


def evaluate_vo0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0045."""
    return run_spec_rule(VO0045BollingerBandWidthExpandingRule, df)
