from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class GateStatus(Enum):
    PASS = "PASS"
    WARNING = "WARNING"
    FAIL = "FAIL"


@dataclass
class GateResult:
    name: str
    status: GateStatus
    reason: str
    deduction: int = 0  # WARNING 상태일 때 적용될 감점 수치


@dataclass
class PipelineResult:
    is_passed: bool
    final_score: int
    total_deduction: int
    gate_results: List[GateResult] = field(default_factory=list)
