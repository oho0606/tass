"""Analyze workflow router (TASS v1 frontend)."""

from __future__ import annotations

import asyncio
import json

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse

from api.deps import get_api_state
from api.schemas.analyze import (
    AnalysisDetailResponse,
    AnalyzeRequest,
    AnalyzeTriggerResponse,
    AnalyzeStatusEvent,
)
from api.services.analysis_detail import build_analysis_detail
from api.services.analyze_job import get_analyze_manager
from api.services.state import TassApiState

router = APIRouter(prefix="/api", tags=["analyze"])


@router.post("/analyze", response_model=AnalyzeTriggerResponse)
def trigger_analyze(
    body: AnalyzeRequest,
    state: TassApiState = Depends(get_api_state),
) -> AnalyzeTriggerResponse:
    """Start universe analysis for the selected timing basis."""
    manager = get_analyze_manager()
    job = manager.start(state, body.mode.value)
    return AnalyzeTriggerResponse(job_id=job.job_id)


@router.get("/analyze/status")
async def analyze_status_stream(
    job_id: str = Query(..., description="Job id returned by POST /api/analyze"),
) -> StreamingResponse:
    """Stream analyze progress via Server-Sent Events."""

    async def event_generator():
        manager = get_analyze_manager()
        while True:
            job = manager.get_job(job_id)
            if job is None:
                payload = AnalyzeStatusEvent(
                    job_id=job_id,
                    status="error",
                    phase="error",
                    progress=0,
                    message="분석 작업을 찾을 수 없습니다",
                    error="job_not_found",
                )
                yield f"data: {json.dumps(payload.model_dump())}\n\n"
                break

            event = AnalyzeStatusEvent(
                job_id=job.job_id,
                status=job.status,
                phase=job.phase,
                progress=job.progress,
                message=job.message,
                error=job.error,
                summary=job.summary.model_dump() if job.summary else None,
                picks=job.picks if job.status == "complete" else None,
                gate_blocked=job.gate_blocked if job.status == "complete" else None,
            )
            yield f"data: {json.dumps(event.model_dump())}\n\n"

            if job.status in ("complete", "error"):
                break
            await asyncio.sleep(0.4)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.get("/analysis/{ticker}", response_model=AnalysisDetailResponse)
def analysis_detail(
    ticker: str,
    state: TassApiState = Depends(get_api_state),
) -> AnalysisDetailResponse:
    """Return Explainable AI report for a ticker from the latest analysis."""
    try:
        return build_analysis_detail(state, ticker)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
