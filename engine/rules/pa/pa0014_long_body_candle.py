"""PA0014 — Long Body Candle. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0014LongBodyCandleRule(SpecRule):
    rule_id = "PA0014"
    rule_name = "Long Body Candle"


def evaluate_pa0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0014."""
    return run_spec_rule(PA0014LongBodyCandleRule, df)
