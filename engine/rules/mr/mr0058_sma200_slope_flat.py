"""MR0058 — SMA200 Slope Flat. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0058SMA200SlopeFlatRule(SpecRule):
    rule_id = "MR0058"
    rule_name = "SMA200 Slope Flat"


def evaluate_mr0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0058."""
    return run_spec_rule(MR0058SMA200SlopeFlatRule, df)
