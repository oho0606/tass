"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { useQuery } from "@tanstack/react-query";
import {
  api,
  analyzeStatusUrl,
  type AnalysisMode,
  type AnalyzeStatusEvent,
  type AnalyzeSummary,
  type PickDetail,
  type PicksHistoryResponse,
} from "./client";

export function useAnalysisDetail(ticker: string) {
  return useQuery({
    queryKey: ["analysis", ticker],
    queryFn: () => api.analysisDetail(ticker),
    enabled: Boolean(ticker),
  });
}

export function useAnalyzeFlow() {
  const [jobId, setJobId] = useState<string | null>(null);
  const [status, setStatus] = useState<AnalyzeStatusEvent["status"]>("idle");
  const [progress, setProgress] = useState(0);
  const [message, setMessage] = useState("");
  const [summary, setSummary] = useState<AnalyzeSummary | null>(null);
  const [picks, setPicks] = useState<PickDetail[]>([]);
  const [gateBlocked, setGateBlocked] = useState<PickDetail[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [mode, setMode] = useState<AnalysisMode>("close");
  const sourceRef = useRef<EventSource | null>(null);

  const reset = useCallback(() => {
    sourceRef.current?.close();
    sourceRef.current = null;
    setJobId(null);
    setStatus("idle");
    setProgress(0);
    setMessage("");
    setSummary(null);
    setPicks([]);
    setGateBlocked([]);
    setError(null);
  }, []);

  const startAnalyze = useCallback(async () => {
    reset();
    setStatus("running");
    setMessage("분석을 시작합니다...");

    try {
      const { job_id } = await api.triggerAnalyze(mode);
      setJobId(job_id);

      const source = new EventSource(analyzeStatusUrl(job_id));
      sourceRef.current = source;

      source.onmessage = (event) => {
        const payload = JSON.parse(event.data) as AnalyzeStatusEvent;
        setStatus(payload.status);
        setProgress(payload.progress);
        setMessage(payload.message);

        if (payload.summary) setSummary(payload.summary);
        if (payload.picks) setPicks(payload.picks);
        if (payload.gate_blocked) setGateBlocked(payload.gate_blocked);
        if (payload.error) setError(payload.error);

        if (payload.status === "complete" || payload.status === "error") {
          source.close();
          sourceRef.current = null;
        }
      };

      source.onerror = () => {
        setError("분석 상태 연결이 끊어졌습니다.");
        setStatus("error");
        source.close();
        sourceRef.current = null;
      };
    } catch (err) {
      setStatus("error");
      setError(err instanceof Error ? err.message : "분석 시작에 실패했습니다.");
    }
  }, [mode, reset]);

  useEffect(() => () => sourceRef.current?.close(), []);

  return {
    mode,
    setMode,
    jobId,
    status,
    progress,
    message,
    summary,
    picks,
    gateBlocked,
    error,
    isRunning: status === "running",
    startAnalyze,
    reset,
  };
}

export function usePicksHistory(limit = 7) {
  return useQuery<PicksHistoryResponse>({
    queryKey: ["picks-history", limit],
    queryFn: () => api.picksHistory(limit),
    staleTime: 30_000,
  });
}
