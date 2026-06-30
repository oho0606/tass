"use client";

import { ANALYSIS_MODE_LABELS, type AnalysisMode } from "@/lib/api/client";
import { cn } from "@/lib/utils";

const MODES: AnalysisMode[] = ["close", "open", "intraday"];

export function SegmentedControl({
  value,
  onChange,
  disabled,
}: {
  value: AnalysisMode;
  onChange: (mode: AnalysisMode) => void;
  disabled?: boolean;
}) {
  return (
    <div className="flex rounded-xl bg-background p-1 ring-1 ring-border">
      {MODES.map((mode) => (
        <button
          key={mode}
          type="button"
          disabled={disabled}
          onClick={() => onChange(mode)}
          className={cn(
            "flex-1 rounded-lg px-2 py-2.5 text-xs font-medium transition-all sm:px-3 sm:text-sm",
            value === mode
              ? "bg-primary text-white shadow-sm"
              : "text-text-secondary hover:text-foreground",
            disabled && "opacity-50",
          )}
        >
          {ANALYSIS_MODE_LABELS[mode]}
        </button>
      ))}
    </div>
  );
}
