"use client";

import { AlertTriangle, ChevronDown, CircleCheck } from "lucide-react";
import { useState } from "react";
import { cn } from "@/lib/utils";

export function AccordionItem({
  title,
  detail,
  scoreDelta,
  passed = true,
  defaultOpen = false,
}: {
  title: string;
  detail: string;
  scoreDelta?: number | null;
  passed?: boolean;
  defaultOpen?: boolean;
}) {
  const [open, setOpen] = useState(defaultOpen);

  return (
    <div className="border-b border-border last:border-b-0">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="flex w-full items-center gap-3 px-1 py-3.5 text-left transition-colors hover:bg-primary/5"
      >
        <CircleCheck
          className={cn(
            "h-5 w-5 shrink-0",
            passed ? "text-success" : "text-text-secondary",
          )}
        />
        <span className="flex-1 text-sm font-medium">{title}</span>
        {scoreDelta != null ? (
          <span className="font-tabular text-sm font-semibold text-success">
            +{scoreDelta}점
          </span>
        ) : null}
        <ChevronDown
          className={cn(
            "h-4 w-4 shrink-0 text-text-secondary transition-transform duration-200",
            open && "rotate-180",
          )}
        />
      </button>
      <div
        className={cn(
          "grid transition-all duration-200 ease-out",
          open ? "grid-rows-[1fr] opacity-100" : "grid-rows-[0fr] opacity-0",
        )}
      >
        <div className="overflow-hidden">
          <p className="pb-3 pl-8 pr-2 text-sm leading-relaxed text-text-secondary">{detail}</p>
        </div>
      </div>
    </div>
  );
}

export function PenaltyAccordionItem({
  title,
  detail,
  scoreDelta,
}: {
  title: string;
  detail: string;
  scoreDelta?: number | null;
}) {
  const [open, setOpen] = useState(false);

  return (
    <div className="rounded-xl border border-danger/25 bg-danger/5">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="flex w-full items-center gap-3 px-4 py-3.5 text-left"
      >
        <AlertTriangle className="h-5 w-5 shrink-0 text-warning" />
        <span className="flex-1 text-sm font-medium text-foreground">{title}</span>
        {scoreDelta != null ? (
          <span className="font-tabular text-sm font-semibold text-danger">{scoreDelta}점</span>
        ) : null}
        <ChevronDown
          className={cn(
            "h-4 w-4 shrink-0 text-text-secondary transition-transform duration-200",
            open && "rotate-180",
          )}
        />
      </button>
      {open ? (
        <p className="border-t border-danger/20 px-4 pb-3.5 pt-2 text-sm leading-relaxed text-text-secondary">
          {detail}
        </p>
      ) : null}
    </div>
  );
}
