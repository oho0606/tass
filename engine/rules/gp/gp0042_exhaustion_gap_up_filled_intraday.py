"""GP0042 — Exhaustion Gap Up Filled Intraday. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0042ExhaustionGapUpFilledIntradayRule(SpecRule):
    rule_id = "GP0042"
    rule_name = "Exhaustion Gap Up Filled Intraday"


def evaluate_gp0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0042."""
    return run_spec_rule(GP0042ExhaustionGapUpFilledIntradayRule, df)
