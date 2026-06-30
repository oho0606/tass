"""CF0033 — Bollinger Band Width Expanding Confirms Breakout. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0033BollingerBandWidthExpandingConfirmsBreakoutRule(SpecRule):
    rule_id = "CF0033"
    rule_name = "Bollinger Band Width Expanding Confirms Breakout"


def evaluate_cf0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0033."""
    return run_spec_rule(CF0033BollingerBandWidthExpandingConfirmsBreakoutRule, df)
