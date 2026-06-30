from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from engine.core.types import RuleResult, RuleVerdict


class BaseCompositeRule(ABC):
    """
    TASS-027 Composite Rule interface.
    Input: Atomic Rule results only. Output: PASS | PARTIAL | FAIL | UNKNOWN.
    Composite rules do not compute scores.
    """

    rule_id: str
    rule_name: str
    version: str = "1.0.0"
    dependencies: tuple[str, ...] = ()

    def evaluate(self, atomic: dict[str, RuleResult]) -> RuleResult:
        missing = self._missing_or_unknown(atomic)
        if missing:
            return self._result("UNKNOWN", [missing], {"precondition_failed": True})
        verdict, reasons, metadata = self.decide(atomic)
        return self._result(verdict, reasons, metadata)

    @abstractmethod
    def decide(
        self, atomic: dict[str, RuleResult]
    ) -> tuple[RuleVerdict, list[str], dict[str, Any]]: ...

    def _missing_or_unknown(self, atomic: dict[str, RuleResult]) -> str | None:
        for dep in self.dependencies:
            if dep not in atomic:
                return f"Missing atomic dependency: {dep}"
            if atomic[dep].verdict == "UNKNOWN":
                return f"Atomic dependency UNKNOWN: {dep}"
        return None

    def _result(
        self,
        verdict: RuleVerdict,
        reasons: list[str],
        metadata: dict[str, Any] | None = None,
    ) -> RuleResult:
        return RuleResult(
            rule_id=self.rule_id,
            verdict=verdict,
            status=verdict,
            score=0.0,
            reasons=reasons,
            metadata=metadata or {},
        )

    def explain(self, result: RuleResult) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "rule_name": self.rule_name,
            "verdict": result.verdict,
            "because": result.metadata,
            "reasons": result.reasons,
        }
