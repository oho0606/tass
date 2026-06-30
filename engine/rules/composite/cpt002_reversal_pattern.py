"""CPT002 — Reversal Pattern. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPT002",
    rule_name="Reversal Pattern",
    atomic_prefix="PT",
    mode="bullish",
)


def evaluate_cpt002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPT002 from atomic rule results."""
    return _RULE.evaluate(atomic)
