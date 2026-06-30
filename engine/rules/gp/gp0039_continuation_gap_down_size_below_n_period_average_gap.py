"""GP0039 — Continuation Gap Down Size Below N-Period Average Gap. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0039ContinuationGapDownSizeBelowNPeriodAverageGapRule(SpecRule):
    rule_id = "GP0039"
    rule_name = "Continuation Gap Down Size Below N-Period Average Gap"


def evaluate_gp0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0039."""
    return run_spec_rule(GP0039ContinuationGapDownSizeBelowNPeriodAverageGapRule, df)
