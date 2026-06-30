"""GP0043 — Exhaustion Gap Up Bar Bearish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0043ExhaustionGapUpBarBearishRule(SpecRule):
    rule_id = "GP0043"
    rule_name = "Exhaustion Gap Up Bar Bearish"


def evaluate_gp0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0043."""
    return run_spec_rule(GP0043ExhaustionGapUpBarBearishRule, df)
