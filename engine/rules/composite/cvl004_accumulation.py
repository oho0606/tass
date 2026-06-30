"""CVL004 — Accumulation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL004",
    rule_name="Accumulation",
    atomic_prefix="VL",
    mode="bullish",
)


def evaluate_cvl004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL004 from atomic rule results."""
    return _RULE.evaluate(atomic)
