"""MR0053 — ADX At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0053ADXAtNPeriodHighRule(SpecRule):
    rule_id = "MR0053"
    rule_name = "ADX At N-Period High"


def evaluate_mr0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0053."""
    return run_spec_rule(MR0053ADXAtNPeriodHighRule, df)
