"""DQ0005 — Volume Missing. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0005VolumeMissingRule(SpecRule):
    rule_id = "DQ0005"
    rule_name = "Volume Missing"


def evaluate_dq0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0005."""
    return run_spec_rule(DQ0005VolumeMissingRule, df)
