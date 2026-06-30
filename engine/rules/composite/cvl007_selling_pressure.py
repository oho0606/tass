"""CVL007 — Selling Pressure. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL007",
    rule_name="Selling Pressure",
    atomic_prefix="VL",
    mode="bearish",
)


def evaluate_cvl007(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL007 from atomic rule results."""
    return _RULE.evaluate(atomic)
