"""CCF005 — Full Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CCF005",
    rule_name="Full Confirmation",
    atomic_prefix="CF",
    mode="quality",
)


def evaluate_ccf005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CCF005 from atomic rule results."""
    return _RULE.evaluate(atomic)
