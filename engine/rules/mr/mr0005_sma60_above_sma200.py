"""MR0005 — SMA60 Above SMA200. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0005SMA60AboveSMA200Rule(SpecRule):
    rule_id = "MR0005"
    rule_name = "SMA60 Above SMA200"


def evaluate_mr0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0005."""
    return run_spec_rule(MR0005SMA60AboveSMA200Rule, df)
