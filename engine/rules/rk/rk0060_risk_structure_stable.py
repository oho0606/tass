"""RK0060 — Risk Structure Stable. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0060RiskStructureStableRule(SpecRule):
    rule_id = "RK0060"
    rule_name = "Risk Structure Stable"


def evaluate_rk0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0060."""
    return run_spec_rule(RK0060RiskStructureStableRule, df)
