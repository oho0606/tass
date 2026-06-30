"""PB0053 — Pullback Range Contracting. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0053PullbackRangeContractingRule(SpecRule):
    rule_id = "PB0053"
    rule_name = "Pullback Range Contracting"


def evaluate_pb0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0053."""
    return run_spec_rule(PB0053PullbackRangeContractingRule, df)
