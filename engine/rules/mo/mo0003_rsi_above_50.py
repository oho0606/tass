"""MO0003 — RSI Above 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0003RSIAbove50Rule(SpecRule):
    rule_id = "MO0003"
    rule_name = "RSI Above 50"


def evaluate_mo0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0003."""
    return run_spec_rule(MO0003RSIAbove50Rule, df)
