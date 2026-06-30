"""MO0044 — MFI Below 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0044MFIBelow50Rule(SpecRule):
    rule_id = "MO0044"
    rule_name = "MFI Below 50"


def evaluate_mo0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0044."""
    return run_spec_rule(MO0044MFIBelow50Rule, df)
