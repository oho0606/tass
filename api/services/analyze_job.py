"""Background analyze job with real pipeline progress via SSE (TASS v1)."""

from __future__ import annotations

import threading
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Literal

from api.schemas.analyze import AnalyzeSummary
from api.schemas.picks import PickDetail
from api.services.state import TassApiState, pick_detail_from_result

JobStatus = Literal["idle", "running", "complete", "error"]


@dataclass
class AnalyzeJob:
    job_id: str
    mode: str
    status: JobStatus = "running"
    phase: str = "init"
    progress: int = 0
    message: str = "분석 준비 중"
    error: str | None = None
    started_at: float = field(default_factory=time.monotonic)
    finished_at: float | None = None
    summary: AnalyzeSummary | None = None
    picks: list[PickDetail] = field(default_factory=list)
    gate_blocked: list[PickDetail] = field(default_factory=list)
    _listeners: list[threading.Condition] = field(default_factory=list)

    def set_progress(self, phase: str, progress: int, message: str) -> None:
        self.phase = phase
        self.progress = progress
        self.message = message
        self._notify()

    def complete(
        self,
        summary: AnalyzeSummary,
        picks: list[PickDetail],
        gate_blocked: list[PickDetail] | None = None,
    ) -> None:
        self.status = "complete"
        self.phase = "complete"
        self.progress = 100
        self.message = "Top 20 추출 완료"
        self.summary = summary
        self.picks = picks
        self.gate_blocked = gate_blocked or []
        self.finished_at = time.monotonic()
        self._notify()

    def fail(self, error: str) -> None:
        self.status = "error"
        self.error = error
        self.message = "분석 중 오류가 발생했습니다"
        self.finished_at = time.monotonic()
        self._notify()

    def _notify(self) -> None:
        for cond in self._listeners:
            with cond:
                cond.notify_all()

    def to_event_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "job_id": self.job_id,
            "status": self.status,
            "phase": self.phase,
            "progress": self.progress,
            "message": self.message,
            "error": self.error,
        }
        if self.summary is not None:
            payload["summary"] = self.summary.model_dump()
        if self.picks:
            payload["picks"] = [p.model_dump() for p in self.picks]
        if self.gate_blocked:
            payload["gate_blocked"] = [p.model_dump() for p in self.gate_blocked]
        return payload


class AnalyzeJobManager:
    """Singleton manager for one active analyze job at a time."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._job: AnalyzeJob | None = None

    def get_job(self, job_id: str) -> AnalyzeJob | None:
        with self._lock:
            if self._job is not None and self._job.job_id == job_id:
                return self._job
            return None

    def current_job(self) -> AnalyzeJob | None:
        with self._lock:
            return self._job

    def start(self, state: TassApiState, mode: str) -> AnalyzeJob:
        with self._lock:
            if self._job is not None and self._job.status == "running":
                return self._job

            job = AnalyzeJob(job_id=str(uuid.uuid4()), mode=mode)
            self._job = job
            thread = threading.Thread(
                target=self._run,
                args=(state, job),
                daemon=True,
                name=f"analyze-{job.job_id[:8]}",
            )
            thread.start()
            return job

    def _run(self, state: TassApiState, job: AnalyzeJob) -> None:
        started = time.monotonic()

        def _pipeline_callback(phase: str, pct: int, msg: str) -> None:
            """Forward engine progress events to the SSE job."""
            # Map engine phases (0–82%) into the final 0–90% band so that
            # "saving" and "complete" still have visible steps at the end.
            mapped = round(pct * 90 / 82) if pct <= 82 else pct
            job.set_progress(phase, min(mapped, 90), msg)

        try:
            job.set_progress("init", 0, "분석 준비 중")

            cache = state.ensure_picks(
                refresh=True,
                progress_callback=_pipeline_callback,
            )

            job.set_progress("saving", 92, "결과 저장 중")

            all_ranked = cache.all_ranked or cache.picks
            passed_count = sum(
                1
                for pick in all_ranked
                if str(pick.gate).upper() in {"PASS", "WARN"}
            )

            top20 = [pick_detail_from_result(p) for p in cache.picks[:20]]
            blocked = [pick_detail_from_result(p) for p in cache.gate_blocked]
            elapsed = round(time.monotonic() - started, 1)

            summary = AnalyzeSummary(
                universe_size=cache.universe_size,
                passed_count=passed_count,
                elapsed_seconds=elapsed,
                analysis_mode=job.mode,
                date=cache.date,
                generated_at=cache.generated_at,
            )
            job.complete(summary, top20, blocked)

        except Exception as exc:  # noqa: BLE001 — surface to SSE client
            job.fail(str(exc))


_analyze_manager: AnalyzeJobManager | None = None


def get_analyze_manager() -> AnalyzeJobManager:
    global _analyze_manager  # noqa: PLW0603
    if _analyze_manager is None:
        _analyze_manager = AnalyzeJobManager()
    return _analyze_manager
