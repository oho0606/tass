import type { components } from "./schema";

// When NEXT_PUBLIC_API_URL is empty (""), requests go to the same origin and
// Next.js rewrites (next.config.ts) proxy them to the backend.
// For local development, set NEXT_PUBLIC_API_URL=http://localhost:8000 in .env.local.
const API_BASE =
  (process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000").replace(/\/$/, "");

async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      ...init?.headers,
    },
    cache: "no-store",
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(body || `API error ${response.status}`);
  }

  return response.json() as Promise<T>;
}

export type HealthResponse = components["schemas"]["HealthResponse"];
export type PickDetail = components["schemas"]["PickDetail"];

export type AnalysisMode = "close" | "open" | "intraday";

export interface AnalyzeSummary {
  universe_size: number;
  passed_count: number;
  elapsed_seconds: number;
  analysis_mode: string;
  date: string;
  generated_at: string;
}

export interface AnalyzeStatusEvent {
  job_id: string;
  status: "idle" | "running" | "complete" | "error";
  phase: string;
  progress: number;
  message: string;
  error?: string | null;
  summary?: AnalyzeSummary | null;
  picks?: PickDetail[] | null;
  gate_blocked?: PickDetail[] | null;
}

export interface RuleAccordionItem {
  title: string;
  score_delta?: number | null;
  detail: string;
  passed?: boolean;
}

export interface PenaltyItem {
  title: string;
  score_delta?: number | null;
  detail: string;
}

export interface AnalysisDetailResponse {
  symbol: string;
  name: string;
  rank?: number | null;
  total_score: number;
  max_score: number;
  recommendation?: string | null;
  summary: string;
  radar: Record<string, number>;
  domains: Array<{
    key: string;
    label: string;
    score: number;
    max_score: number;
  }>;
  rules: RuleAccordionItem[];
  penalties: PenaltyItem[];
}

export interface PicksHistoryItem {
  date: string;
  generated_at: string;
  mvp_mode: boolean;
  universe_size: number;
  candidates_evaluated: number;
  picks_count: number;
  gate_blocked_count: number;
  top_symbols: string[];
}

export interface PicksHistoryResponse {
  items: PicksHistoryItem[];
}

export const api = {
  health: () => apiFetch<HealthResponse>("/health"),
  triggerAnalyze: (mode: AnalysisMode) =>
    apiFetch<{ job_id: string }>("/api/analyze", {
      method: "POST",
      body: JSON.stringify({ mode }),
    }),
  analysisDetail: (ticker: string) =>
    apiFetch<AnalysisDetailResponse>(`/api/analysis/${encodeURIComponent(ticker)}`),
  picksHistory: (limit = 7) =>
    apiFetch<PicksHistoryResponse>(`/picks/history?limit=${encodeURIComponent(String(limit))}`),
};

export function analyzeStatusUrl(jobId: string): string {
  return `${API_BASE}/api/analyze/status?job_id=${encodeURIComponent(jobId)}`;
}

export const ANALYSIS_MODE_LABELS: Record<AnalysisMode, string> = {
  close: "종가 분석",
  open: "시가 분석",
  intraday: "장중 분석",
};
