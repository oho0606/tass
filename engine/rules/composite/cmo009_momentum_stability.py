"""CMO009 — Momentum Stability. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMO009",
    rule_name="Momentum Stability",
    atomic_prefix="MO",
    mode="quality",
)


def evaluate_cmo009(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMO009 from atomic rule results."""
    return _RULE.evaluate(atomic)
