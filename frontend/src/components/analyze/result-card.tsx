import { ChevronRight } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { RankBadge } from "@/components/ui/rank-badge";
import type { PickDetail } from "@/lib/api/client";
import {
  oneLineSummary,
  recommendationVariant,
  simplifyRecommendation,
} from "@/lib/ui-helpers";
import { cn } from "@/lib/utils";

export function ResultRow({
  pick,
  style,
}: {
  pick: PickDetail;
  style?: React.CSSProperties;
}) {
  return (
    <a
      href={`/stock/${pick.symbol}`}
      className={cn(
        "group flex items-center gap-3 border-b border-border px-3 py-3.5 transition-colors last:border-b-0",
        "hover:bg-primary/5 animate-fade-in-up",
      )}
      style={style}
    >
      <RankBadge rank={pick.rank} />

      <div className="min-w-0 flex-1">
        <div className="flex items-baseline gap-2">
          <span className="truncate font-semibold">{pick.name}</span>
          <span className="shrink-0 font-tabular text-xs text-text-secondary">{pick.symbol}</span>
        </div>
        <p className="mt-0.5 hidden truncate text-xs text-text-secondary sm:block">
          {oneLineSummary(pick)}
        </p>
      </div>

      <div className="flex shrink-0 items-center gap-2 sm:gap-3">
        <span className="font-tabular text-lg font-bold text-success sm:text-xl">
          {pick.total_score.toFixed(0)}
          <span className="ml-0.5 text-xs font-normal text-text-secondary">점</span>
        </span>
        {pick.recommendation ? (
          <Badge variant={recommendationVariant(pick.recommendation)} className="min-w-[52px] justify-center">
            {simplifyRecommendation(pick.recommendation)}
          </Badge>
        ) : null}
        <ChevronRight className="h-4 w-4 text-text-secondary transition-transform group-hover:translate-x-0.5 group-hover:text-primary" />
      </div>
    </a>
  );
}
