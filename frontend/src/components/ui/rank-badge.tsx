import { cn } from "@/lib/utils";

const RANK_STYLES: Record<number, string> = {
  1: "bg-gold/20 text-gold ring-gold/40",
  2: "bg-silver/15 text-silver ring-silver/30",
  3: "bg-bronze/20 text-bronze ring-bronze/40",
};

export function RankBadge({ rank }: { rank: number }) {
  const style = RANK_STYLES[rank];

  return (
    <span
      className={cn(
        "flex h-8 w-8 shrink-0 items-center justify-center rounded-full font-tabular text-sm font-bold ring-1",
        style ?? "bg-primary/10 text-primary ring-primary/20",
      )}
    >
      {rank}
    </span>
  );
}
