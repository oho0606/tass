"use client";

import dynamic from "next/dynamic";
import { Skeleton } from "@/components/ui/skeleton";
import type { AnalysisDetailResponse } from "@/lib/api/client";

type RadarData = Pick<AnalysisDetailResponse, "symbol" | "name" | "domains" | "radar">;

const ReactECharts = dynamic(() => import("echarts-for-react"), {
  ssr: false,
  loading: () => <Skeleton className="h-64 w-full" />,
});

export function DomainRadarChart({ data }: { data: RadarData }) {
  const labels = Object.keys(data.radar);
  const values = Object.values(data.radar);

  const option = {
    backgroundColor: "transparent",
    tooltip: {},
    radar: {
      indicator: labels.map((name) => ({ name, max: 100 })),
      radius: "68%",
      splitArea: { areaStyle: { color: ["#1c2129", "#161b22"] } },
      axisName: { color: "#8b949e", fontSize: 11 },
      splitLine: { lineStyle: { color: "#2d333b" } },
      axisLine: { lineStyle: { color: "#2d333b" } },
    },
    series: [
      {
        type: "radar",
        data: [
          {
            value: values,
            name: data.name,
            areaStyle: { color: "rgba(59,130,246,0.2)" },
            lineStyle: { color: "#3b82f6", width: 2 },
            itemStyle: { color: "#60a5fa" },
          },
        ],
      },
    ],
  };

  return (
    <div className="grid gap-4 lg:grid-cols-[1fr_200px]">
      <ReactECharts option={option} style={{ height: 280, width: "100%" }} />
      <div className="grid grid-cols-2 gap-2 lg:grid-cols-1">
        {data.domains.map((domain) => (
          <div
            key={domain.key}
            className="flex items-center justify-between rounded-lg bg-background px-3 py-2"
          >
            <span className="text-xs text-text-secondary">{domain.label}</span>
            <span className="font-tabular text-sm font-semibold text-success">
              {domain.score.toFixed(0)}
              <span className="text-xs font-normal text-text-secondary">
                /{domain.max_score.toFixed(0)}
              </span>
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
