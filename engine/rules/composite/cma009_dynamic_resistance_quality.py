"""CMA009 — Dynamic Resistance Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMA009",
    rule_name="Dynamic Resistance Quality",
    atomic_prefix="MA",
    mode="bearish",
)


def evaluate_cma009(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMA009 from atomic rule results."""
    return _RULE.evaluate(atomic)
