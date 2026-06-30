import type { AnalyzeSummary, PickDetail } from "@/lib/api/client";
import { GateBlockedRow } from "./gate-blocked-row";
import { ResultRow } from "./result-card";
import { SummaryBar } from "./summary-bar";

export function ResultList({
  summary,
  picks,
  gateBlocked = [],
}: {
  summary: AnalyzeSummary;
  picks: PickDetail[];
  gateBlocked?: PickDetail[];
}) {
  if (!picks.length) {
    return (
      <div className="glass-card rounded-2xl p-10 text-center">
        <p className="text-base leading-relaxed text-text-secondary">
          현재 시장 상황에서 시스템 기준을 통과한 안정적인 종목이 없습니다.
        </p>
      </div>
    );
  }

  return (
    <section className="space-y-4 animate-fade-in-up">
      <SummaryBar summary={summary} />

      <div className="glass-card overflow-hidden rounded-2xl">
        <div className="border-b border-border px-4 py-3">
          <h2 className="text-sm font-semibold">Top 20 추천 종목</h2>
          <p className="text-xs text-text-secondary">종목을 탭하여 추천 근거를 확인하세요</p>
        </div>
        <div>
          {picks.map((pick, index) => (
            <ResultRow
              key={pick.symbol}
              pick={pick}
              style={{ animationDelay: `${index * 50}ms` }}
            />
          ))}
        </div>
      </div>

      {gateBlocked.length > 0 ? (
        <div className="glass-card overflow-hidden rounded-2xl">
          <div className="border-b border-border px-4 py-3">
            <h2 className="text-sm font-semibold">Gate 차단 관찰 목록</h2>
            <p className="text-xs text-text-secondary">
              점수는 높지만 pipeline gate FAIL로 Today&apos;s Picks에서 제외된 종목입니다
            </p>
          </div>
          <div>
            {gateBlocked.map((pick) => (
              <GateBlockedRow key={pick.symbol} pick={pick} />
            ))}
          </div>
        </div>
      ) : null}
    </section>
  );
}
