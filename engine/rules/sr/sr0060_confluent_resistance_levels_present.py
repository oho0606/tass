"""SR0060 — Confluent Resistance Levels Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0060ConfluentResistanceLevelsPresentRule(SpecRule):
    rule_id = "SR0060"
    rule_name = "Confluent Resistance Levels Present"


def evaluate_sr0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0060."""
    return run_spec_rule(SR0060ConfluentResistanceLevelsPresentRule, df)
