"""DQ0035 — Zero Volume Session. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0035ZeroVolumeSessionRule(SpecRule):
    rule_id = "DQ0035"
    rule_name = "Zero Volume Session"


def evaluate_dq0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0035."""
    return run_spec_rule(DQ0035ZeroVolumeSessionRule, df)
