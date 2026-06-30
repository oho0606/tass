"""MO0035 — CCI Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0035CCIRisingRule(SpecRule):
    rule_id = "MO0035"
    rule_name = "CCI Rising"


def evaluate_mo0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0035."""
    return run_spec_rule(MO0035CCIRisingRule, df)
