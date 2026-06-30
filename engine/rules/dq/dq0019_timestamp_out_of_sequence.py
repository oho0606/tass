"""DQ0019 — Timestamp Out of Sequence. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0019TimestampOutofSequenceRule(SpecRule):
    rule_id = "DQ0019"
    rule_name = "Timestamp Out of Sequence"


def evaluate_dq0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0019."""
    return run_spec_rule(DQ0019TimestampOutofSequenceRule, df)
