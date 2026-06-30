from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import pandas as pd

from engine.core.types import RuleResult, RuleVerdict


class BaseRule(ABC):
    """
    TASS-012 Rule interface.
    One Rule · One Class · One File · No global state · No side effects.
    """

    rule_id: str
    rule_name: str
    version: str = "1.0.0"

    def __init__(self) -> None:
        self._parameters: dict[str, Any] = {}
        self._calculation: dict[str, Any] = {}
        self._last_result: RuleResult | None = None

    def initialize(self, parameters: dict[str, Any] | None = None) -> None:
        """Load parameters (no hard-coded overrides without defaults)."""
        self._parameters = {**self.default_parameters(), **(parameters or {})}
        self._calculation = {}
        self._last_result = None

    @abstractmethod
    def default_parameters(self) -> dict[str, Any]: ...

    @abstractmethod
    def validate_input(self, df: pd.DataFrame) -> bool:
        """Return False if preconditions fail (caller returns UNKNOWN)."""
        ...

    @abstractmethod
    def calculate(self, df: pd.DataFrame) -> dict[str, Any]:
        """Deterministic calculation; store intermediates in returned dict."""
        ...

    @abstractmethod
    def evaluate(self, df: pd.DataFrame) -> RuleVerdict:
        """PASS | FAIL | UNKNOWN based on calculate() output."""
        ...

    def run(self, df: pd.DataFrame) -> RuleResult:
        """Full pipeline: validate → calculate → evaluate → result."""
        if not self.validate_input(df):
            self._last_result = self._unknown_result("Preconditions not met")
            return self._last_result
        self._calculation = self.calculate(df)
        verdict = self.evaluate(df)
        self._last_result = self.result(verdict)
        return self._last_result

    def result(self, verdict: RuleVerdict | None = None) -> RuleResult:
        if self._last_result is not None and verdict is None:
            return self._last_result
        return self._build_result(verdict or "FAIL")

    @abstractmethod
    def _build_result(self, verdict: RuleVerdict) -> RuleResult: ...

    def metadata(self) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "rule_name": self.rule_name,
            "version": self.version,
            "parameters": dict(self._parameters),
            "calculation": dict(self._calculation),
        }

    def _unknown_result(self, reason: str) -> RuleResult:
        return RuleResult(
            rule_id=self.rule_id,
            verdict="UNKNOWN",
            status="UNKNOWN",
            score=0.0,
            reasons=[reason],
            metadata={"precondition_failed": True},
        )

    def explain(self) -> dict[str, Any]:
        """Machine-readable explainability (TASS-012 §12)."""
        r = self._last_result
        if r is None:
            return {"verdict": "UNKNOWN", "because": {}}
        return {
            "verdict": r.verdict,
            "because": r.metadata,
            "reasons": r.reasons,
        }
