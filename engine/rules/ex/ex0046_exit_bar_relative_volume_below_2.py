"""EX0046 — Exit Bar Relative Volume Below 2. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0046ExitBarRelativeVolumeBelow2Rule(SpecRule):
    rule_id = "EX0046"
    rule_name = "Exit Bar Relative Volume Below 2"


def evaluate_ex0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0046."""
    return run_spec_rule(EX0046ExitBarRelativeVolumeBelow2Rule, df)
