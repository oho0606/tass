"""DQ0018 — Identical OHLC Values. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0018IdenticalOHLCValuesRule(SpecRule):
    rule_id = "DQ0018"
    rule_name = "Identical OHLC Values"


def evaluate_dq0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0018."""
    return run_spec_rule(DQ0018IdenticalOHLCValuesRule, df)
