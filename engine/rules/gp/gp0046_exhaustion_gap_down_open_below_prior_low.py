"""GP0046 — Exhaustion Gap Down Open Below Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0046ExhaustionGapDownOpenBelowPriorLowRule(SpecRule):
    rule_id = "GP0046"
    rule_name = "Exhaustion Gap Down Open Below Prior Low"


def evaluate_gp0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0046."""
    return run_spec_rule(GP0046ExhaustionGapDownOpenBelowPriorLowRule, df)
