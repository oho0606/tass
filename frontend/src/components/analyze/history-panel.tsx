"use client";

import type { PicksHistoryItem } from "@/lib/api/client";

function fmtTime(value: string): string {
  const dt = new Date(value);
  if (Number.isNaN(dt.getTime())) {
    return value;
  }
  return dt.toLocaleString("ko-KR", {
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  });
}

export function HistoryPanel({ items }: { items: PicksHistoryItem[] }) {
  if (!items.length) {
    return null;
  }

  return (
    <section className="glass-card overflow-hidden rounded-2xl">
      <div className="border-b border-border px-4 py-3">
        <h2 className="text-sm font-semibold">최근 추천 이력</h2>
        <p className="text-xs text-text-secondary">최근 분석일의 Top 종목 요약</p>
      </div>
      <div>
        {items.map((item) => (
          <div
            key={`${item.date}-${item.generated_at}`}
            className="grid grid-cols-[1fr_auto] gap-3 border-b border-border/60 px-4 py-3 last:border-b-0"
          >
            <div className="min-w-0">
              <p className="font-tabular text-sm font-semibold">{item.date}</p>
              <p className="mt-0.5 truncate text-xs text-text-secondary">
                Top: {item.top_symbols.join(", ") || "-"}
              </p>
            </div>
            <div className="text-right">
              <p className="font-tabular text-xs text-text-secondary">{fmtTime(item.generated_at)}</p>
              <p className="mt-0.5 text-xs">
                picks {item.picks_count} / blocked {item.gate_blocked_count}
              </p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
