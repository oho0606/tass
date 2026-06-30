"""MO0060 — Momentum Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0060MomentumFallingRule(SpecRule):
    rule_id = "MO0060"
    rule_name = "Momentum Falling"


def evaluate_mo0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0060."""
    return run_spec_rule(MO0060MomentumFallingRule, df)
