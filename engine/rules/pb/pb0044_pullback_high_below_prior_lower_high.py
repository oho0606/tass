"""PB0044 — Pullback High Below Prior Lower High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0044PullbackHighBelowPriorLowerHighRule(SpecRule):
    rule_id = "PB0044"
    rule_name = "Pullback High Below Prior Lower High"


def evaluate_pb0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0044."""
    return run_spec_rule(PB0044PullbackHighBelowPriorLowerHighRule, df)
