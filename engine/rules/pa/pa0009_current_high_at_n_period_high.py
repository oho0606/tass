"""PA0009 — Current High At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0009CurrentHighAtNPeriodHighRule(SpecRule):
    rule_id = "PA0009"
    rule_name = "Current High At N-Period High"


def evaluate_pa0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0009."""
    return run_spec_rule(PA0009CurrentHighAtNPeriodHighRule, df)
