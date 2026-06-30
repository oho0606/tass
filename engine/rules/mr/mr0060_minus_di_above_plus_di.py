"""MR0060 — Minus DI Above Plus DI. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0060MinusDIAbovePlusDIRule(SpecRule):
    rule_id = "MR0060"
    rule_name = "Minus DI Above Plus DI"


def evaluate_mr0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0060."""
    return run_spec_rule(MR0060MinusDIAbovePlusDIRule, df)
