"""RK0005 — ATR At 20-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0005ATRAt20PeriodHighRule(SpecRule):
    rule_id = "RK0005"
    rule_name = "ATR At 20-Period High"


def evaluate_rk0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0005."""
    return run_spec_rule(RK0005ATRAt20PeriodHighRule, df)
