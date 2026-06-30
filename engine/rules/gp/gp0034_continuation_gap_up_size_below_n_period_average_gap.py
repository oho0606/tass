"""GP0034 — Continuation Gap Up Size Below N-Period Average Gap. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0034ContinuationGapUpSizeBelowNPeriodAverageGapRule(SpecRule):
    rule_id = "GP0034"
    rule_name = "Continuation Gap Up Size Below N-Period Average Gap"


def evaluate_gp0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0034."""
    return run_spec_rule(GP0034ContinuationGapUpSizeBelowNPeriodAverageGapRule, df)
