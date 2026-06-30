"""DQ0006 — OHLC All Missing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0006OHLCAllMissingRule(SpecRule):
    rule_id = "DQ0006"
    rule_name = "OHLC All Missing"


def evaluate_dq0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0006."""
    return run_spec_rule(DQ0006OHLCAllMissingRule, df)
