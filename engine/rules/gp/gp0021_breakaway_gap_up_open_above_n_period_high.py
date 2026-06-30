"""GP0021 — Breakaway Gap Up Open Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0021BreakawayGapUpOpenAboveNPeriodHighRule(SpecRule):
    rule_id = "GP0021"
    rule_name = "Breakaway Gap Up Open Above N-Period High"


def evaluate_gp0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0021."""
    return run_spec_rule(GP0021BreakawayGapUpOpenAboveNPeriodHighRule, df)
