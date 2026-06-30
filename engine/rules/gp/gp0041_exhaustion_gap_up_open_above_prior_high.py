"""GP0041 — Exhaustion Gap Up Open Above Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0041ExhaustionGapUpOpenAbovePriorHighRule(SpecRule):
    rule_id = "GP0041"
    rule_name = "Exhaustion Gap Up Open Above Prior High"


def evaluate_gp0041(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0041."""
    return run_spec_rule(GP0041ExhaustionGapUpOpenAbovePriorHighRule, df)
