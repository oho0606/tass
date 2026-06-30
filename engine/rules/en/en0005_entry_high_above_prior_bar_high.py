"""EN0005 — Entry High Above Prior Bar High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0005EntryHighAbovePriorBarHighRule(SpecRule):
    rule_id = "EN0005"
    rule_name = "Entry High Above Prior Bar High"


def evaluate_en0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0005."""
    return run_spec_rule(EN0005EntryHighAbovePriorBarHighRule, df)
