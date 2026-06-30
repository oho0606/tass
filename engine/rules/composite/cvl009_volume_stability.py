"""CVL009 — Volume Stability. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL009",
    rule_name="Volume Stability",
    atomic_prefix="VL",
    mode="quality",
)


def evaluate_cvl009(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL009 from atomic rule results."""
    return _RULE.evaluate(atomic)
