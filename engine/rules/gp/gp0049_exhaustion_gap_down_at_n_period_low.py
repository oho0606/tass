"""GP0049 — Exhaustion Gap Down At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0049ExhaustionGapDownAtNPeriodLowRule(SpecRule):
    rule_id = "GP0049"
    rule_name = "Exhaustion Gap Down At N-Period Low"


def evaluate_gp0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0049."""
    return run_spec_rule(GP0049ExhaustionGapDownAtNPeriodLowRule, df)
