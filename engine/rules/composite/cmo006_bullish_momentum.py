"""CMO006 — Bullish Momentum. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMO006",
    rule_name="Bullish Momentum",
    atomic_prefix="MO",
    mode="bullish",
)


def evaluate_cmo006(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMO006 from atomic rule results."""
    return _RULE.evaluate(atomic)
