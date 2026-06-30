"""GP0050 — Exhaustion Gap Down Size Exceeds N-Period Average Gap. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0050ExhaustionGapDownSizeExceedsNPeriodAverageGapRule(SpecRule):
    rule_id = "GP0050"
    rule_name = "Exhaustion Gap Down Size Exceeds N-Period Average Gap"


def evaluate_gp0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0050."""
    return run_spec_rule(GP0050ExhaustionGapDownSizeExceedsNPeriodAverageGapRule, df)
