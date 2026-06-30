from __future__ import annotations

from typing import Any, Callable, Dict, List

from engine.gate.models import GateResult, GateStatus, PipelineResult


class GatePipeline:
    def __init__(self):
        # TASS-006 명세에 맞춘 엄격한 순차 실행 리스트
        self.gates: List[Callable[[Dict[str, Any], Dict[str, Any]], GateResult]] = []

    def add_gate(self, gate_func: Callable[[Dict[str, Any], Dict[str, Any]], GateResult]):
        """Gate를 파이프라인에 추가 (추가된 순서대로 실행됨)"""
        self.gates.append(gate_func)

    def evaluate_gate_pipeline(
        self, data: Dict[str, Any], config: Dict[str, Any], initial_score: int
    ) -> PipelineResult:
        """순차 중단(Short-circuit) 방식으로 Gate 실행 및 감점 계산"""
        total_deduction = 0
        gate_results = []

        for gate in self.gates:
            result = gate(data, config)
            gate_results.append(result)

            if result.status == GateStatus.FAIL:
                # FAIL 발생 시 즉시 종료 (Short-Circuit)
                return PipelineResult(
                    is_passed=False,
                    final_score=0,
                    total_deduction=total_deduction,
                    gate_results=gate_results,
                )
            elif result.status == GateStatus.WARNING:
                # WARNING 발생 시 추천은 유지하되 감점 누적
                total_deduction += result.deduction

        # 모든 Gate를 통과한 경우 최종 점수 계산 (음수 방지)
        final_score = max(0, initial_score - total_deduction)

        return PipelineResult(
            is_passed=True,
            final_score=final_score,
            total_deduction=total_deduction,
            gate_results=gate_results,
        )
