"""MR0057 — SMA200 Slope Steep. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0057SMA200SlopeSteepRule(SpecRule):
    rule_id = "MR0057"
    rule_name = "SMA200 Slope Steep"


def evaluate_mr0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0057."""
    return run_spec_rule(MR0057SMA200SlopeSteepRule, df)
