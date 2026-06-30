"""MO0042 — MFI Below 20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0042MFIBelow20Rule(SpecRule):
    rule_id = "MO0042"
    rule_name = "MFI Below 20"


def evaluate_mo0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0042."""
    return run_spec_rule(MO0042MFIBelow20Rule, df)
