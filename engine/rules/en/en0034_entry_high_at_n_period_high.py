"""EN0034 — Entry High At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0034EntryHighAtNPeriodHighRule(SpecRule):
    rule_id = "EN0034"
    rule_name = "Entry High At N-Period High"


def evaluate_en0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0034."""
    return run_spec_rule(EN0034EntryHighAtNPeriodHighRule, df)
