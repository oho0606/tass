"""MR0022 — SMA20 Flat. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0022SMA20FlatRule(SpecRule):
    rule_id = "MR0022"
    rule_name = "SMA20 Flat"


def evaluate_mr0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0022."""
    return run_spec_rule(MR0022SMA20FlatRule, df)
