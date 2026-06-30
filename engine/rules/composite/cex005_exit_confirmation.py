"""CEX005 — Exit Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CEX005",
    rule_name="Exit Confirmation",
    atomic_prefix="EX",
    mode="quality",
)


def evaluate_cex005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CEX005 from atomic rule results."""
    return _RULE.evaluate(atomic)
