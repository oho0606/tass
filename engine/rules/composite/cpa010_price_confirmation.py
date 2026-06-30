"""CPA010 — Price Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA010",
    rule_name="Price Confirmation",
    atomic_prefix="PA",
    mode="quality",
)


def evaluate_cpa010(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA010 from atomic rule results."""
    return _RULE.evaluate(atomic)
