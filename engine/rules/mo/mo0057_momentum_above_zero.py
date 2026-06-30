"""MO0057 — Momentum Above Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0057MomentumAboveZeroRule(SpecRule):
    rule_id = "MO0057"
    rule_name = "Momentum Above Zero"


def evaluate_mo0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0057."""
    return run_spec_rule(MO0057MomentumAboveZeroRule, df)
