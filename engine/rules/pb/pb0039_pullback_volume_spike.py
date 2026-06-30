"""PB0039 — Pullback Volume Spike. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0039PullbackVolumeSpikeRule(SpecRule):
    rule_id = "PB0039"
    rule_name = "Pullback Volume Spike"


def evaluate_pb0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0039."""
    return run_spec_rule(PB0039PullbackVolumeSpikeRule, df)
