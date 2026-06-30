"""PA0012 — Bearish Candle. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0012BearishCandleRule(SpecRule):
    rule_id = "PA0012"
    rule_name = "Bearish Candle"


def evaluate_pa0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0012."""
    return run_spec_rule(PA0012BearishCandleRule, df)
