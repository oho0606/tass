"""CSR001 — Support Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CSR001",
    rule_name="Support Quality",
    atomic_prefix="SR",
    mode="quality",
)


def evaluate_csr001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CSR001 from atomic rule results."""
    return _RULE.evaluate(atomic)
