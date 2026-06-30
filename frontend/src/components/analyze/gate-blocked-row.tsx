import { AlertTriangle } from "lucide-react";
import type { PickDetail } from "@/lib/api/client";

export function GateBlockedRow({ pick }: { pick: PickDetail }) {
  const reason = pick.reasons?.[0] ?? "Pipeline gate FAIL";

  return (
    <div className="flex items-start gap-3 border-b border-border px-4 py-3 last:border-b-0">
      <AlertTriangle className="mt-0.5 h-4 w-4 shrink-0 text-warning" />
      <div className="min-w-0 flex-1">
        <div className="flex items-baseline gap-2">
          <span className="truncate font-medium text-text-secondary">{pick.name}</span>
          <span className="shrink-0 font-tabular text-xs text-text-secondary">{pick.symbol}</span>
        </div>
        <p className="mt-0.5 text-xs text-text-secondary">{reason}</p>
      </div>
      <span className="shrink-0 font-tabular text-sm text-text-secondary">
        {pick.total_score.toFixed(0)}점
      </span>
    </div>
  );
}
