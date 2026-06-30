"""DQ0043 — Volume Spike Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0043VolumeSpikePresentRule(SpecRule):
    rule_id = "DQ0043"
    rule_name = "Volume Spike Present"


def evaluate_dq0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0043."""
    return run_spec_rule(DQ0043VolumeSpikePresentRule, df)
