"""CMA004 — Death Cross Strength. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMA004",
    rule_name="Death Cross Strength",
    atomic_prefix="MA",
    mode="bearish",
)


def evaluate_cma004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMA004 from atomic rule results."""
    return _RULE.evaluate(atomic)
