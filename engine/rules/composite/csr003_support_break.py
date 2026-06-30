"""CSR003 — Support Break. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CSR003",
    rule_name="Support Break",
    atomic_prefix="SR",
    mode="quality",
)


def evaluate_csr003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CSR003 from atomic rule results."""
    return _RULE.evaluate(atomic)
