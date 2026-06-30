"""CVL006 — Buying Pressure. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL006",
    rule_name="Buying Pressure",
    atomic_prefix="VL",
    mode="bullish",
)


def evaluate_cvl006(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL006 from atomic rule results."""
    return _RULE.evaluate(atomic)
