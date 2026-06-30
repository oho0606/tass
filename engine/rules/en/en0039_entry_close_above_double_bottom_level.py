"""EN0039 — Entry Close Above Double Bottom Level. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0039EntryCloseAboveDoubleBottomLevelRule(SpecRule):
    rule_id = "EN0039"
    rule_name = "Entry Close Above Double Bottom Level"


def evaluate_en0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0039."""
    return run_spec_rule(EN0039EntryCloseAboveDoubleBottomLevelRule, df)
