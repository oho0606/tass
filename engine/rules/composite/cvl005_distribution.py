"""CVL005 — Distribution. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL005",
    rule_name="Distribution",
    atomic_prefix="VL",
    mode="bearish",
)


def evaluate_cvl005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL005 from atomic rule results."""
    return _RULE.evaluate(atomic)
