"""PB0047 — Pullback Low Above Rising SMA. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0047PullbackLowAboveRisingSMARule(SpecRule):
    rule_id = "PB0047"
    rule_name = "Pullback Low Above Rising SMA"


def evaluate_pb0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0047."""
    return run_spec_rule(PB0047PullbackLowAboveRisingSMARule, df)
