"""PB0043 — Pullback Low Above Prior Higher Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0043PullbackLowAbovePriorHigherLowRule(SpecRule):
    rule_id = "PB0043"
    rule_name = "Pullback Low Above Prior Higher Low"


def evaluate_pb0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0043."""
    return run_spec_rule(PB0043PullbackLowAbovePriorHigherLowRule, df)
