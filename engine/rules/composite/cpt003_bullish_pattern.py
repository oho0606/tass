"""CPT003 — Bullish Pattern. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPT003",
    rule_name="Bullish Pattern",
    atomic_prefix="PT",
    mode="bullish",
)


def evaluate_cpt003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPT003 from atomic rule results."""
    return _RULE.evaluate(atomic)
