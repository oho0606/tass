"""PB0040 — Pullback Volume Flat. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0040PullbackVolumeFlatRule(SpecRule):
    rule_id = "PB0040"
    rule_name = "Pullback Volume Flat"


def evaluate_pb0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0040."""
    return run_spec_rule(PB0040PullbackVolumeFlatRule, df)
