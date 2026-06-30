"""GP0047 — Exhaustion Gap Down Filled Intraday. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0047ExhaustionGapDownFilledIntradayRule(SpecRule):
    rule_id = "GP0047"
    rule_name = "Exhaustion Gap Down Filled Intraday"


def evaluate_gp0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0047."""
    return run_spec_rule(GP0047ExhaustionGapDownFilledIntradayRule, df)
