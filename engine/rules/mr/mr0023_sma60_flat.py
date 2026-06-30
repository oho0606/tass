"""MR0023 — SMA60 Flat. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0023SMA60FlatRule(SpecRule):
    rule_id = "MR0023"
    rule_name = "SMA60 Flat"


def evaluate_mr0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0023."""
    return run_spec_rule(MR0023SMA60FlatRule, df)
