"""VL0047 — Price Up Volume Up. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import PriceVolumeAgreementRule, run_confirmation_rule


class VL0047PriceUpVolumeUpRule(PriceVolumeAgreementRule):
    rule_id = "VL0047"
    rule_name = "Price Up Volume Up"
    mode = "up_up"


def evaluate_vl0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0047."""
    return run_confirmation_rule(VL0047PriceUpVolumeUpRule, df)
