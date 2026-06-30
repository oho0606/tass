"""PB0005 — Pullback Low Above Prior Swing Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0005PullbackLowAbovePriorSwingLowRule(SpecRule):
    rule_id = "PB0005"
    rule_name = "Pullback Low Above Prior Swing Low"


def evaluate_pb0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0005."""
    return run_spec_rule(PB0005PullbackLowAbovePriorSwingLowRule, df)
