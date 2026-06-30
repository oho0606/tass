"""CSR005 — Dynamic Support Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CSR005",
    rule_name="Dynamic Support Quality",
    atomic_prefix="SR",
    mode="quality",
)


def evaluate_csr005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CSR005 from atomic rule results."""
    return _RULE.evaluate(atomic)
