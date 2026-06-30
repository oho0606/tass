"""GP0022 — Breakaway Gap Up Low Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0022BreakawayGapUpLowAboveNPeriodHighRule(SpecRule):
    rule_id = "GP0022"
    rule_name = "Breakaway Gap Up Low Above N-Period High"


def evaluate_gp0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0022."""
    return run_spec_rule(GP0022BreakawayGapUpLowAboveNPeriodHighRule, df)
