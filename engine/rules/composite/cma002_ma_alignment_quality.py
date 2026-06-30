"""CMA002 — MA Alignment Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMA002",
    rule_name="MA Alignment Quality",
    atomic_prefix="MA",
    mode="quality",
)


def evaluate_cma002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMA002 from atomic rule results."""
    return _RULE.evaluate(atomic)
