"""CVL002 — Volume Expansion. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL002",
    rule_name="Volume Expansion",
    atomic_prefix="VL",
    mode="bullish",
)


def evaluate_cvl002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL002 from atomic rule results."""
    return _RULE.evaluate(atomic)
