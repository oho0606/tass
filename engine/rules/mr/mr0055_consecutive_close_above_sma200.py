"""MR0055 — Consecutive Close Above SMA200. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0055ConsecutiveCloseAboveSMA200Rule(SpecRule):
    rule_id = "MR0055"
    rule_name = "Consecutive Close Above SMA200"


def evaluate_mr0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0055."""
    return run_spec_rule(MR0055ConsecutiveCloseAboveSMA200Rule, df)
