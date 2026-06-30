import { ANALYSIS_MODE_LABELS, type AnalyzeSummary } from "@/lib/api/client";

export function SummaryBar({ summary }: { summary: AnalyzeSummary }) {
  const modeLabel = ANALYSIS_MODE_LABELS[summary.analysis_mode as keyof typeof ANALYSIS_MODE_LABELS] ?? summary.analysis_mode;

  const items = [
    { label: "분석 대상", value: `${summary.universe_size.toLocaleString()}개` },
    { label: "조건 통과", value: `${summary.passed_count}개` },
    { label: "분석 시간", value: `${summary.elapsed_seconds}초` },
    { label: "분석 기준", value: modeLabel },
  ];

  return (
    <div className="grid grid-cols-2 gap-px overflow-hidden rounded-xl bg-border sm:grid-cols-4">
      {items.map((item) => (
        <div key={item.label} className="bg-card px-3 py-3 text-center sm:px-4">
          <p className="text-[10px] text-text-secondary sm:text-xs">{item.label}</p>
          <p className="mt-0.5 font-tabular text-sm font-semibold text-foreground sm:text-base">
            {item.value}
          </p>
        </div>
      ))}
    </div>
  );
}
