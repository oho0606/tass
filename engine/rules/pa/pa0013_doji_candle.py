"""PA0013 — Doji Candle. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0013DojiCandleRule(SpecRule):
    rule_id = "PA0013"
    rule_name = "Doji Candle"


def evaluate_pa0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0013."""
    return run_spec_rule(PA0013DojiCandleRule, df)
