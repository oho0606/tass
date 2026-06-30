"""MR0039 — Volatility Above Prior Period. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0039VolatilityAbovePriorPeriodRule(SpecRule):
    rule_id = "MR0039"
    rule_name = "Volatility Above Prior Period"


def evaluate_mr0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0039."""
    return run_spec_rule(MR0039VolatilityAbovePriorPeriodRule, df)
