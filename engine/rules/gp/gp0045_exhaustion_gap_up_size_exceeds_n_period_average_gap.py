"""GP0045 — Exhaustion Gap Up Size Exceeds N-Period Average Gap. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0045ExhaustionGapUpSizeExceedsNPeriodAverageGapRule(SpecRule):
    rule_id = "GP0045"
    rule_name = "Exhaustion Gap Up Size Exceeds N-Period Average Gap"


def evaluate_gp0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0045."""
    return run_spec_rule(GP0045ExhaustionGapUpSizeExceedsNPeriodAverageGapRule, df)
