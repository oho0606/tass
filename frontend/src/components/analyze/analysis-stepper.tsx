"use client";

import { BarChart3, Check, Cog, Database, Trophy } from "lucide-react";
import { cn } from "@/lib/utils";
import { Progress } from "@/components/ui/progress";

const STEPS = [
  { id: "loading", label: "데이터 로드", threshold: 10, Icon: Database },
  { id: "rules", label: "Rule Engine", threshold: 45, Icon: Cog },
  { id: "domains", label: "Domain 점수", threshold: 80, Icon: BarChart3 },
  { id: "complete", label: "Top 20 추출", threshold: 100, Icon: Trophy },
] as const;

function stepState(progress: number, threshold: number, index: number): "done" | "active" | "pending" {
  if (progress >= threshold) return "done";
  const prevThreshold = index === 0 ? 0 : STEPS[index - 1].threshold;
  if (progress >= prevThreshold) return "active";
  return "pending";
}

export function AnalysisStepper({
  progress,
  visible,
}: {
  progress: number;
  visible: boolean;
}) {
  if (!visible) return null;

  return (
    <div className="space-y-4">
      <div className="grid grid-cols-4 gap-1 sm:gap-2">
        {STEPS.map((step, index) => {
          const state = stepState(progress, step.threshold, index);
          const { Icon } = step;

          return (
            <div key={step.id} className="flex flex-col items-center gap-1.5 text-center">
              <div
                className={cn(
                  "flex h-9 w-9 items-center justify-center rounded-full transition-all duration-300 sm:h-10 sm:w-10",
                  state === "done" && "bg-success/20 text-success",
                  state === "active" && "bg-primary/20 text-primary ring-2 ring-primary/50",
                  state === "pending" && "bg-border/50 text-text-secondary",
                )}
              >
                {state === "done" ? (
                  <Check className="h-4 w-4" />
                ) : (
                  <Icon className="h-4 w-4" />
                )}
              </div>
              <p
                className={cn(
                  "text-[10px] leading-tight sm:text-xs",
                  state === "active" ? "font-medium text-foreground" : "text-text-secondary",
                )}
              >
                {step.label}
              </p>
              <p className="font-tabular text-[10px] text-text-secondary">{step.threshold}%</p>
            </div>
          );
        })}
      </div>
      <Progress value={progress} className="h-1.5" />
    </div>
  );
}
