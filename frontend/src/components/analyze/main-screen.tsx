"use client";

import { Play } from "lucide-react";
import { useEffect, useState } from "react";
import { HistoryPanel } from "@/components/analyze/history-panel";
import { AnalysisStepper } from "@/components/analyze/analysis-stepper";
import { ResultList } from "@/components/analyze/result-list";
import { SegmentedControl } from "@/components/analyze/segmented-control";
import { Skeleton } from "@/components/ui/skeleton";
import { useAnalyzeFlow, usePicksHistory } from "@/lib/api/hooks";

function ServerClock() {
  const [now, setNow] = useState<string>("");

  useEffect(() => {
    const tick = () => {
      setNow(
        new Date().toLocaleString("ko-KR", {
          year: "numeric",
          month: "2-digit",
          day: "2-digit",
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
          hour12: false,
        }),
      );
    };
    tick();
    const id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, []);

  if (!now) return <Skeleton className="h-4 w-36" />;
  return <p className="font-tabular text-xs text-text-secondary">{now}</p>;
}

export function MainScreen() {
  const historyQuery = usePicksHistory(5);
  const {
    mode,
    setMode,
    status,
    progress,
    message,
    summary,
    picks,
    gateBlocked,
    error,
    isRunning,
    startAnalyze,
  } = useAnalyzeFlow();

  const showResults = status === "complete" && summary;
  const showStepper = isRunning || status === "complete";

  return (
    <div className="space-y-6">
      <header className="flex items-center justify-between gap-4">
        <h1 className="text-2xl font-bold tracking-tight">
          <span className="text-primary">TASS</span>
        </h1>
        <ServerClock />
      </header>

      <div className="glass-card space-y-6 rounded-2xl p-5 sm:p-6">
        <section className="space-y-3">
          <p className="text-xs font-medium text-text-secondary">분석 기준 선택</p>
          <SegmentedControl value={mode} onChange={setMode} disabled={isRunning} />
        </section>

        <section className="flex flex-col items-center gap-3 py-2">
          <button
            type="button"
            disabled={isRunning}
            onClick={() => void startAnalyze()}
            className="analyze-btn-glow flex h-14 w-full max-w-md items-center justify-center gap-2.5 rounded-2xl bg-primary text-base font-semibold text-white transition hover:bg-primary/90 disabled:opacity-60 sm:h-16 sm:text-lg"
          >
            <Play className="h-5 w-5 fill-current" />
            {isRunning ? "분석 진행 중..." : "분석 시작"}
          </button>
          <p className="text-center text-xs text-text-secondary">
            백엔드 Rule Engine이 자동으로 적용됩니다
          </p>
        </section>

        {showStepper ? (
          <section className="space-y-3 border-t border-border pt-5">
            <AnalysisStepper progress={progress} visible />
            {message && isRunning ? (
              <p className="text-center text-xs text-text-secondary">{message}</p>
            ) : null}
            {error ? <p className="text-center text-sm text-danger">{error}</p> : null}
          </section>
        ) : null}
      </div>

      {showResults ? (
        <ResultList summary={summary} picks={picks} gateBlocked={gateBlocked} />
      ) : null}

      {!historyQuery.isLoading && historyQuery.data?.items?.length ? (
        <HistoryPanel items={historyQuery.data.items} />
      ) : null}
    </div>
  );
}
