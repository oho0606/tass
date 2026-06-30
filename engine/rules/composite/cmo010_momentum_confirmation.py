"""CMO010 — Momentum Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMO010",
    rule_name="Momentum Confirmation",
    atomic_prefix="MO",
    mode="quality",
)


def evaluate_cmo010(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMO010 from atomic rule results."""
    return _RULE.evaluate(atomic)
