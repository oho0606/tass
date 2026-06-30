"""CPA001 — Price Strength. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA001",
    rule_name="Price Strength",
    atomic_prefix="PA",
    mode="bullish",
)


def evaluate_cpa001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA001 from atomic rule results."""
    return _RULE.evaluate(atomic)
