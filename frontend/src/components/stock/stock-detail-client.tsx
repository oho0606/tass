"use client";

import { ArrowLeft } from "lucide-react";
import Link from "next/link";
import { DomainRadarChart } from "@/components/stock/domain-radar-chart";
import { AccordionItem, PenaltyAccordionItem } from "@/components/ui/accordion";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { useAnalysisDetail } from "@/lib/api/hooks";
import { recommendationVariant, simplifyRecommendation } from "@/lib/ui-helpers";

function DetailSkeleton() {
  return (
    <div className="space-y-4">
      <Skeleton className="h-6 w-24" />
      <Skeleton className="h-20 w-full rounded-2xl" />
      <Skeleton className="h-32 w-full rounded-2xl" />
      <Skeleton className="h-72 w-full rounded-2xl" />
      <Skeleton className="h-48 w-full rounded-2xl" />
    </div>
  );
}

export function StockDetailClient({ code }: { code: string }) {
  const { data, isLoading, error } = useAnalysisDetail(code);

  if (isLoading) return <DetailSkeleton />;

  if (error || !data) {
    return (
      <div className="space-y-3">
        <Link
          href="/"
          className="inline-flex items-center gap-1.5 text-sm text-primary hover:underline"
        >
          <ArrowLeft className="h-4 w-4" />
          목록으로
        </Link>
        <p className="text-danger">종목 정보를 불러올 수 없습니다.</p>
      </div>
    );
  }

  return (
    <div className="space-y-5 animate-fade-in-up">
      <Link
        href="/"
        className="inline-flex items-center gap-1.5 text-sm text-text-secondary transition hover:text-primary"
      >
        <ArrowLeft className="h-4 w-4" />
        목록으로
      </Link>

      <header className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold">{data.name}</h1>
          <p className="font-tabular text-sm text-text-secondary">{data.symbol}</p>
        </div>
        <div className="flex items-center gap-3">
          {data.recommendation ? (
            <Badge
              variant={recommendationVariant(data.recommendation)}
              className="px-4 py-1 text-sm"
            >
              {simplifyRecommendation(data.recommendation)}
            </Badge>
          ) : null}
          <div className="text-right">
            <p className="font-tabular text-3xl font-bold text-success sm:text-4xl">
              {data.total_score.toFixed(0)}
              <span className="text-base font-normal text-text-secondary">점</span>
            </p>
          </div>
        </div>
      </header>

      <div className="glass-card rounded-2xl p-5">
        <h2 className="mb-2 text-xs font-medium text-text-secondary">AI 종합 요약</h2>
        <p className="text-sm leading-relaxed text-foreground/90">{data.summary}</p>
      </div>

      <div className="glass-card rounded-2xl p-5">
        <h2 className="mb-4 text-sm font-semibold">도메인 점수</h2>
        <DomainRadarChart
          data={{
            symbol: data.symbol,
            name: data.name,
            domains: data.domains,
            radar: data.radar,
          }}
        />
      </div>

      <div className="glass-card overflow-hidden rounded-2xl">
        <div className="border-b border-border px-5 py-3.5">
          <h2 className="text-sm font-semibold">핵심 룰 통과</h2>
          <p className="text-xs text-text-secondary">추천 이유 (Explainable AI)</p>
        </div>
        <div className="px-4">
          {data.rules.length ? (
            data.rules.map((rule) => (
              <AccordionItem
                key={rule.title}
                title={rule.title}
                detail={rule.detail}
                scoreDelta={rule.score_delta}
                passed={rule.passed ?? true}
              />
            ))
          ) : (
            <p className="py-6 text-center text-sm text-text-secondary">
              통과한 규칙 정보가 없습니다.
            </p>
          )}
        </div>
      </div>

      {data.penalties.length ? (
        <section className="space-y-3">
          <h2 className="text-sm font-semibold text-warning">위험 및 감점 요소</h2>
          {data.penalties.map((penalty) => (
            <PenaltyAccordionItem
              key={penalty.title}
              title={penalty.title}
              detail={penalty.detail}
              scoreDelta={penalty.score_delta}
            />
          ))}
        </section>
      ) : null}
    </div>
  );
}
