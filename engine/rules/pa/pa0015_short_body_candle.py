"""PA0015 — Short Body Candle. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0015ShortBodyCandleRule(SpecRule):
    rule_id = "PA0015"
    rule_name = "Short Body Candle"


def evaluate_pa0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0015."""
    return run_spec_rule(PA0015ShortBodyCandleRule, df)
