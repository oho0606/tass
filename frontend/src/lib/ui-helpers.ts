import type { PickDetail } from "@/lib/api/client";

export function recommendationVariant(rec: string | null | undefined) {
  const upper = (rec ?? "").toUpperCase();
  if (upper.includes("BUY")) return "positive" as const;
  if (upper.includes("HOLD") || upper.includes("WATCH")) return "warning" as const;
  if (upper.includes("SELL")) return "negative" as const;
  return "primary" as const;
}

export function oneLineSummary(pick: PickDetail): string {
  const reasons = pick.recommendation_reason ?? pick.reasons ?? [];
  return reasons[0] ?? "Rule Engine 조건을 통과한 종목입니다.";
}

export function simplifyRecommendation(rec: string | null | undefined): string {
  if (!rec) return "—";
  const upper = rec.toUpperCase();
  if (upper.includes("STRONG BUY") || upper === "BUY") return "BUY";
  if (upper.includes("HOLD") || upper.includes("WATCH")) return "HOLD";
  if (upper.includes("SELL")) return "SELL";
  return rec;
}
