"""MR0032 — ATR At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0032ATRAtNPeriodHighRule(SpecRule):
    rule_id = "MR0032"
    rule_name = "ATR At N-Period High"


def evaluate_mr0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0032."""
    return run_spec_rule(MR0032ATRAtNPeriodHighRule, df)
