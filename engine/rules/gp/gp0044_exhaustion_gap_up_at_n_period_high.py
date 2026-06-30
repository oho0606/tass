"""GP0044 — Exhaustion Gap Up At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0044ExhaustionGapUpAtNPeriodHighRule(SpecRule):
    rule_id = "GP0044"
    rule_name = "Exhaustion Gap Up At N-Period High"


def evaluate_gp0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0044."""
    return run_spec_rule(GP0044ExhaustionGapUpAtNPeriodHighRule, df)
